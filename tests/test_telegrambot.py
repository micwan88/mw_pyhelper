import unittest
from unittest.mock import patch, MagicMock

from mw_pyhelper.messaging.telegrambot import TelegramBot
from mw_pyhelper.network.proxyselector import ProxySelector

TOKEN = 'dummy-token'
CHAT_IDS = ['12345']
PROXY = {'http': 'http://a:8080', 'https': 'http://a:8080'}


def _ok_response() -> MagicMock:
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {'ok': True}
    return response


class TestTelegramBot(unittest.TestCase):
    @patch('mw_pyhelper.messaging.telegrambot.requests.post')
    def test_postmsg_without_proxy(self, mock_post: MagicMock):
        mock_post.return_value = _ok_response()
        bot = TelegramBot(TOKEN)

        result = bot.postmsg(CHAT_IDS, 'hello')

        self.assertEqual(result, 0)
        self.assertEqual(mock_post.call_args.kwargs['proxies'], None)

    @patch('mw_pyhelper.messaging.telegrambot.requests.post')
    def test_postmsg_with_proxy(self, mock_post: MagicMock):
        mock_post.return_value = _ok_response()
        bot = TelegramBot(TOKEN, proxy_selector=ProxySelector([PROXY]))

        result = bot.postmsg(CHAT_IDS, 'hello')

        self.assertEqual(result, 0)
        self.assertEqual(mock_post.call_args.kwargs['proxies'], PROXY)

    @patch('mw_pyhelper.messaging.telegrambot.requests.post')
    def test_postmsg_with_botname_prefixes_and_escapes(self, mock_post: MagicMock):
        mock_post.return_value = _ok_response()
        bot = TelegramBot(TOKEN, botname='MyBot')

        result = bot.postmsg(CHAT_IDS, 'a < b & c')

        self.assertEqual(result, 0)
        sent_text = mock_post.call_args.kwargs['json']['text']
        self.assertEqual(sent_text, 'MyBot:a &lt; b &amp; c')

    @patch('mw_pyhelper.messaging.telegrambot.requests.post')
    def test_postmsg_http_error_returns_minus_one(self, mock_post: MagicMock):
        response = MagicMock()
        response.status_code = 400
        response.text = 'bad request'
        mock_post.return_value = response
        bot = TelegramBot(TOKEN)

        self.assertEqual(bot.postmsg(CHAT_IDS, 'hello'), -1)


if __name__ == '__main__':
    unittest.main()
