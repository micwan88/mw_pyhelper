import logging
from typing import Dict, List, Optional


class ProxySelector():
    def __init__(self, proxy_list: List[Dict[str, str]], is_round_robin: bool = False) -> None:
        self.proxy_list = proxy_list
        self.is_round_robin = is_round_robin
        self.next_index = 0

        # Init logger for whole class
        self.mylogger = logging.getLogger(__name__)

    @classmethod
    def from_protocol(cls, protocol: str, proxy_url_list: List[str],
                      is_round_robin: bool = False) -> 'ProxySelector':
        proxy_list: List[Dict[str, str]] = [{protocol: proxy_url} for proxy_url in proxy_url_list]
        return cls(proxy_list, is_round_robin)

    def getproxy(self) -> Optional[Dict[str, str]]:
        if not self.proxy_list:
            self.mylogger.debug('getproxy called with empty proxy list, return None')
            return None

        if not self.is_round_robin:
            return self.proxy_list[0]

        proxy = self.proxy_list[self.next_index]
        self.next_index = (self.next_index + 1) % len(self.proxy_list)
        self.mylogger.debug('getproxy round-robin selected: %s' % proxy)
        return proxy
