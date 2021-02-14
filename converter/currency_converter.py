""" Module implementing converting currencies class """

# internal modules
import re
from typing import Dict, Optional, Union
from urllib import request

#project modules
from logger import get_custom_logger
from .validator import validate_params_list, ValidationError


logger = get_custom_logger(__name__)


class ConverterClient:

    """
    Class for connecting with currencies service and converting currencies

    Default currencies are USD and RUB
    """

    def __init__(self):
        self.url = "https://www.profinance.ru/currency_usd.asp"
        self.currency_reg = r'<tdclass=cellalign=centercolspan=\"2\"><fontcolor=\"Red\"><b>([0-9]*\.[0-9]*)</b>'

        self.usd_value = self._get_current_usd_value()
        self.currencies = ["USD", "RUB"]

    def get_currencies_dict(self, path: str) -> Union[Dict[str, str], str]:

        """
        Method for generating dict object with params from request
        """

        try:
            params = validate_params_list(path.split("?", 1)[1].split("&"))
            currencies_params = {param.split("=")[0]: param.split("=")[1] for param in params}
            result = self._get_converted_result_dict(currencies_params)
            logger.info("GET request with parametrs: %s", currencies_params)
        except (IndexError, ValidationError) as exc:
            msg = "Incorrect request with incorrect parameters: %s" % str(exc)
            logger.warning(msg)
            result = msg

        return result

    def _get_current_usd_value(self) -> Optional[int]:
        with request.urlopen(url=self.url) as res:
            data = res.read().decode('utf-8')
            data = ''.join(data.split())
            new = re.search(self.currency_reg, data)

        try:
            new = float(new.group(1))
        except:
            new = None
        return new

    def _get_converted_result_dict(self, currencies_data: Dict[str, str]) \
                                  -> Union[Dict[str, Union[str, int, float]], str]:
        result = {"start_value": currencies_data["value"]}

        if all((currencies_data["from"] in self.currencies,
                currencies_data["to"] in self.currencies)):
            result["converting_type"] = f"{currencies_data['from']} > {currencies_data['to']}"
        else:
            msg = "Incorrect currencies types! \
                Must be RUB and USD, given %s, %s" \
                % (currencies_data["from"], currencies_data["to"])
            logger.error(msg)
            return msg

        converting_result = self._count_result_value(currencies_data["value"],
                                                 result["converting_type"])

        if isinstance(converting_result, str):
            return converting_result

        result["result_value"] = converting_result
        return result

    def _count_result_value(self, value: str, converting_type: str) -> Union[float, str]:
        try:
            value = float(value)
        except ValueError as err:
            msg = "Invalid type of currency value! %s" % str(err)
            logger.error(msg)
            return msg

        try:
            if converting_type == "RUB > USD":
                result = value / self.usd_value
            elif converting_type == "USD > RUB":
                result = value * self.usd_value
            return round(result, 2)
        except TypeError as err:
            msg = "Invalid type of USD value! %s" % str(err)
            logger.error(msg)
            return msg
