import unittest

from mw_pyhelper.network.proxyselector import ProxySelector

PROXY_A = {'http': 'http://a:8080', 'https': 'http://a:8080'}
PROXY_B = {'http': 'http://b:8080', 'https': 'http://b:8080'}


class TestProxySelector(unittest.TestCase):
    def test_list_constructor_no_round_robin_always_first(self):
        selector = ProxySelector([PROXY_A, PROXY_B])
        self.assertEqual(selector.getproxy(), PROXY_A)
        self.assertEqual(selector.getproxy(), PROXY_A)
        self.assertEqual(selector.getproxy(), PROXY_A)

    def test_list_constructor_round_robin_cycles(self):
        selector = ProxySelector([PROXY_A, PROXY_B], is_round_robin=True)
        self.assertEqual(selector.getproxy(), PROXY_A)
        self.assertEqual(selector.getproxy(), PROXY_B)
        self.assertEqual(selector.getproxy(), PROXY_A)
        self.assertEqual(selector.getproxy(), PROXY_B)

    def test_round_robin_single_proxy(self):
        selector = ProxySelector([PROXY_A], is_round_robin=True)
        self.assertEqual(selector.getproxy(), PROXY_A)
        self.assertEqual(selector.getproxy(), PROXY_A)

    def test_from_protocol_builds_dict_list(self):
        selector = ProxySelector.from_protocol('http', ['http://a:8080', 'http://b:8080'])
        self.assertEqual(selector.proxy_list,
                         [{'http': 'http://a:8080'}, {'http': 'http://b:8080'}])
        # default is not round-robin -> always first
        self.assertEqual(selector.getproxy(), {'http': 'http://a:8080'})
        self.assertEqual(selector.getproxy(), {'http': 'http://a:8080'})

    def test_from_protocol_round_robin(self):
        selector = ProxySelector.from_protocol(
            'https', ['http://a:8080', 'http://b:8080'], is_round_robin=True)
        self.assertEqual(selector.getproxy(), {'https': 'http://a:8080'})
        self.assertEqual(selector.getproxy(), {'https': 'http://b:8080'})
        self.assertEqual(selector.getproxy(), {'https': 'http://a:8080'})

    def test_empty_list_returns_none(self):
        self.assertIsNone(ProxySelector([]).getproxy())
        self.assertIsNone(ProxySelector([], is_round_robin=True).getproxy())
        self.assertIsNone(ProxySelector.from_protocol('http', []).getproxy())


if __name__ == '__main__':
    unittest.main()
