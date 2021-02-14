"""Module implementing http handler """

from http import server
from urllib.parse import urlparse

from logger import get_custom_logger
from .currency_converter import ConverterClient


logger = get_custom_logger(__name__)


class ConverterHTTPHandler(server.SimpleHTTPRequestHandler):
    converter = ConverterClient()

    def do_GET(self):
        currencies = self.converter.get_currencies(self.path)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
