from mw_pyhelper.network.proxyselector import ProxySelector

PROXY_A = {'http': 'http://a:8080', 'https': 'http://a:8080'}
PROXY_B = {'http': 'http://b:8080', 'https': 'http://b:8080'}


def test_list_constructor_no_round_robin_always_first():
    selector = ProxySelector([PROXY_A, PROXY_B])
    assert selector.getproxy() == PROXY_A
    assert selector.getproxy() == PROXY_A
    assert selector.getproxy() == PROXY_A


def test_list_constructor_round_robin_cycles():
    selector = ProxySelector([PROXY_A, PROXY_B], is_round_robin=True)
    assert selector.getproxy() == PROXY_A
    assert selector.getproxy() == PROXY_B
    assert selector.getproxy() == PROXY_A
    assert selector.getproxy() == PROXY_B


def test_round_robin_single_proxy():
    selector = ProxySelector([PROXY_A], is_round_robin=True)
    assert selector.getproxy() == PROXY_A
    assert selector.getproxy() == PROXY_A


def test_from_protocol_builds_dict_list():
    selector = ProxySelector.from_protocol('http', ['http://a:8080', 'http://b:8080'])
    assert selector.proxy_list == [{'http': 'http://a:8080'}, {'http': 'http://b:8080'}]
    # default is not round-robin -> always first
    assert selector.getproxy() == {'http': 'http://a:8080'}
    assert selector.getproxy() == {'http': 'http://a:8080'}


def test_from_protocol_round_robin():
    selector = ProxySelector.from_protocol(
        'https', ['http://a:8080', 'http://b:8080'], is_round_robin=True)
    assert selector.getproxy() == {'https': 'http://a:8080'}
    assert selector.getproxy() == {'https': 'http://b:8080'}
    assert selector.getproxy() == {'https': 'http://a:8080'}


def test_empty_list_returns_none():
    assert ProxySelector([]).getproxy() is None
    assert ProxySelector([], is_round_robin=True).getproxy() is None
    assert ProxySelector.from_protocol('http', []).getproxy() is None
