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
        self.assertEqual(self.obj.get_currencies("/?from=RUB&to=USD&value=20"), {"from": "RUB", "to": "USD", "value": "20"})

    def test_get_currencies_with_exception(self):
        self.assertTrue(self.obj.get_currencies("/%from=RUB&to=USD&value=10") is None)
        self.assertTrue(self.obj.get_currencies("/?from=RUB&to=USD*value=") is None)
        self.assertTrue(self.obj.get_currencies("/fromRUB&to&USD") is None)


if __name__ == "__main__":
    main()
