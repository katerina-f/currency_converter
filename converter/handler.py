"""Module implementing http handler """

import json
from http import server
from urllib.parse import urlparse

from logger import get_custom_logger
from .currency_converter import ConverterClient


class ConverterHTTPHandler(server.SimpleHTTPRequestHandler):
    converter = ConverterClient()

    def do_GET(self):
        currencies_data = self.converter.get_currencies_dict(self.path)
        code = 400 if isinstance(currencies_data, str) else 200
        data = currencies_data if isinstance(currencies_data, str) else json.dumps(currencies_data)
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(data.encode())
