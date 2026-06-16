import logging
import requests
from typing import Optional
from .proxyselector import ProxySelector

URL_IPIFY_API_IPV4 = r'https://api.ipify.org?format=json'
URL_IPIFY_API_IPV6 = r'https://api6.ipify.org?format=json'

def get_ip_addr(is_ipv4: bool = True, proxy_selector: Optional[ProxySelector] = None) -> Optional[str]:
    mylogger = logging.getLogger(__name__)

    api_url = URL_IPIFY_API_IPV4 if is_ipv4 else URL_IPIFY_API_IPV6

    proxies = proxy_selector.getproxy() if proxy_selector is not None else None

    mylogger.debug(f'Calling ip-api service url: {api_url}')
    response = requests.get(api_url, proxies=proxies)
    if response.status_code != requests.codes.ok:
        mylogger.debug(f'get_ip_addr error with {api_url}: {response.text}')
        return None
    
    json_response = response.json()
    return json_response['ip']
