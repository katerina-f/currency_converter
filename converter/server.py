"""Module implementing http server"""

from http import server
from urllib.parse import urlparse

from logger import get_custom_logger
from .validator import validate_params_list, ValidationError


logger = get_custom_logger(__name__)


class ConverterHTTPServer(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        currencies = self.__get_currencies()

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def __get_currencies(self) -> dict:

        """
        Method for generating dict object with params from request
        """

        try:
            params = validate_params_list(self.path.split("?", 1)[1].split("&"))
            currencies = {param.split("=")[0]: param.split("=")[1] for param in params}
            logger.info(f"GET request with parametrs: {currencies}")
        except (IndexError, ValidationError) as exc:
            logger.warning(f"Incorrect request with incorrect parameters: {str(exc)}")
            currencies = {}
        finally:
            return currencies
