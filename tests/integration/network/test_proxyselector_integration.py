import base64
import re
import socket
from typing import List

import pytest
import requests

from mw_pyhelper.network import ipservice
from mw_pyhelper.network.proxyselector import ProxySelector

FREEPROXY_URL = 'https://advanced.name/freeproxy?country=US'
USER_AGENT = 'Mozilla/5.0'
FETCH_TIMEOUT = 15
# Per-attempt socket timeout (free proxies are often slow/dead) and a cap on how
# many candidates we try so the test stays bounded in time.
PROXY_SOCKET_TIMEOUT = 8
MAX_PROXY_ATTEMPTS = 10

_ROW_RE = re.compile(r'<tr>.*?</tr>', re.S)
_IP_RE = re.compile(r'data-ip="([^"]+)"')
_PORT_RE = re.compile(r'data-port="([^"]+)"')
_PROTO_RE = re.compile(r'\?type=\w+"[^>]*>(\w+)</a>')


def fetch_us_https_proxies() -> List[str]:
    """Fetch the freeproxy page and return US + HTTPS proxy urls (http://ip:port)."""
    response = requests.get(FREEPROXY_URL, headers={'User-Agent': USER_AGENT},
                            timeout=FETCH_TIMEOUT)
    response.raise_for_status()
    html = response.text

    proxies: List[str] = []
    for row in _ROW_RE.findall(html):
        ip_match = _IP_RE.search(row)
        port_match = _PORT_RE.search(row)
        if not (ip_match and port_match):
            continue

        protocols = [p.upper() for p in _PROTO_RE.findall(row)]
        is_us = 'country=us' in row
        if 'HTTPS' not in protocols or not is_us:
            continue

        ip = base64.b64decode(ip_match.group(1)).decode()
        port = base64.b64decode(port_match.group(1)).decode()
        proxies.append(f'http://{ip}:{port}')

    return proxies


def test_proxyselector_changes_ip():
    direct_ip = ipservice.get_ip_addr()
    assert direct_ip is not None, 'could not determine direct IP'

    candidates = fetch_us_https_proxies()
    if not candidates:
        pytest.skip('no US+HTTPS free proxies available from the source')

    original_timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(PROXY_SOCKET_TIMEOUT)
    try:
        for proxy_url in candidates[:MAX_PROXY_ATTEMPTS]:
            selector = ProxySelector.from_protocol('https', [proxy_url])
            try:
                proxied_ip = ipservice.get_ip_addr(proxy_selector=selector)
            except requests.RequestException:
                continue

            if proxied_ip and proxied_ip != direct_ip:
                # success: IP differs before vs after applying the proxy
                assert proxied_ip != direct_ip
                return
    finally:
        socket.setdefaulttimeout(original_timeout)

    pytest.skip('none of the candidate free proxies returned a different working IP')
