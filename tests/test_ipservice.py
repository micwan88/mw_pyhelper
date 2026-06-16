import unittest
from unittest.mock import patch, MagicMock

from mw_pyhelper.network import ipservice
from mw_pyhelper.network.proxyselector import ProxySelector

PROXY = {'http': 'http://a:8080', 'https': 'http://a:8080'}


def _ok_response(ip: str) -> MagicMock:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {'ip': ip}
    return response


class TestIpService(unittest.TestCase):
    @patch('mw_pyhelper.network.ipservice.requests.get')
    def test_get_ip_addr_without_proxy(self, mock_get: MagicMock):
        mock_get.return_value = _ok_response('1.1.1.1')

        result = ipservice.get_ip_addr()

        self.assertEqual(result, '1.1.1.1')
        mock_get.assert_called_once_with(ipservice.URL_IPIFY_API_IPV4, proxies=None)

    @patch('mw_pyhelper.network.ipservice.requests.get')
    def test_get_ip_addr_ipv6_without_proxy(self, mock_get: MagicMock):
        mock_get.return_value = _ok_response('::1')

        result = ipservice.get_ip_addr(is_ipv4=False)

        self.assertEqual(result, '::1')
        mock_get.assert_called_once_with(ipservice.URL_IPIFY_API_IPV6, proxies=None)

    @patch('mw_pyhelper.network.ipservice.requests.get')
    def test_get_ip_addr_with_proxy(self, mock_get: MagicMock):
        mock_get.return_value = _ok_response('2.2.2.2')
        selector = ProxySelector([PROXY])

        result = ipservice.get_ip_addr(proxy_selector=selector)

        self.assertEqual(result, '2.2.2.2')
        mock_get.assert_called_once_with(ipservice.URL_IPIFY_API_IPV4, proxies=PROXY)

    @patch('mw_pyhelper.network.ipservice.requests.get')
    def test_get_ip_addr_error_returns_none(self, mock_get: MagicMock):
        response = MagicMock()
        response.status_code = 500
        response.text = 'server error'
        mock_get.return_value = response

        self.assertIsNone(ipservice.get_ip_addr())


if __name__ == '__main__':
    unittest.main()
