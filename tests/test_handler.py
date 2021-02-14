from unittest import TestCase, main

from unittest.mock import MagicMock, patch

from converter.handler import ConverterHTTPHandler
from converter.currency_converter import ConverterClient
from .test_data import MockRequest


class TestHTTPServer(TestCase):

    @patch("converter.currency_converter.ConverterClient.get_currencies")
    def test_do_GET(self, get_currencies):
        self.obj = ConverterHTTPHandler(MockRequest(b'/'), ("", 80), None)
        get_currencies.assert_called_once()


if __name__ == "__main__":
    main()
