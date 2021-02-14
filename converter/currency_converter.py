# internal modules
import urllib

#project modules
from logger import get_custom_logger
from .validator import validate_params_list, ValidationError


logger = get_custom_logger(__name__)


class ConverterClient:

    def __init__(self):
        pass

    def get_currencies(self, path: str) -> dict:

        """
        Method for generating dict object with params from request
        """

        try:
            params = validate_params_list(path.split("?", 1)[1].split("&"))
            currencies = {param.split("=")[0]: param.split("=")[1] for param in params}
            logger.info(f"GET request with parametrs: {currencies}")
        except (IndexError, ValidationError) as exc:
            logger.warning(f"Incorrect request with incorrect parameters: {str(exc)}")
            currencies = None
        finally:
            return currencies
