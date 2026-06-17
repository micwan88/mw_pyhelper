import ipaddress

from mw_pyhelper.network import ipservice


def test_get_ip_addr_returns_real_ip():
    result = ipservice.get_ip_addr()

    assert result is not None, 'ipservice returned no IP'
    # raises ValueError if not a valid IP address
    ipaddress.ip_address(result)
