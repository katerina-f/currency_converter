# internal modules
from socketserver import BaseServer
from unittest import TestCase, main
from unittest.mock import Mock, MagicMock

#project modules
from converter.currency_converter import ConverterClient
from converter.validator import ValidationError


class TestConverterClient(TestCase):

    def setUp(self):
        self.obj = ConverterClient()

    def test_get_currencies(self):
        self.obj.usd_value = 10
        self.assertEqual(self.obj.get_currencies_dict("/?from=RUB&to=USD&value=20"), {"converting_type": "RUB > USD", "start_value": float(20), "result_value": float(2)})

    def test_get_currencies_with_exception(self):
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/%from=RUB&to=USD&value=10"), str))
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/?from=RUB&to=USD*value="), str))
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/fromRUB&to&USD"), str))


if __name__ == "__main__":
    main()
