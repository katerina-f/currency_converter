# internal modules
from socketserver import BaseServer
from unittest import TestCase, main
from unittest.mock import patch

#project modules
from converter.currency_converter import ConverterClient

from .test_data import wrong_values_params, \
                       right_values_params, \
                       wrong_params_for_count


class TestConverterClient(TestCase):

    def setUp(self):
        self.obj = ConverterClient()

    @patch("converter.currency_converter.logger")
    def test_get_currencies(self, logger):
        self.obj.usd_value = 10
        self.assertEqual(self.obj.get_currencies_dict("/?from=RUB&to=USD&value=20"), {"converting_type": "RUB > USD", "start_value": float(20), "result_value": float(2)})

    @patch("converter.currency_converter.logger")
    def test_get_currencies_with_exception(self, logger):
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/%from=RUB&to=USD&value=10"), str))
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/?from=RUB&to=USD*value="), str))
        self.assertTrue(isinstance(self.obj.get_currencies_dict("/fromRUB&to&USD"), str))

    @patch("converter.currency_converter.logger")
    def test_get_converted_result_dict_with_exception(self, logger):
        for params_dict in wrong_values_params:
            with self.subTest(msg=f"test with {params_dict}"):
                self.assertTrue(isinstance(self.obj._get_converted_result_dict(params_dict), str))

    @patch("converter.currency_converter.logger")
    def test_get_converted_result_dict(self, logger):
        self.obj.usd_value = 10
        for params_dict in right_values_params:
            with self.subTest(msg=f"test with {params_dict}"):
                self.assertTrue(isinstance(self.obj._get_converted_result_dict(params_dict), dict))
                self.assertEqual(self.obj._get_converted_result_dict(params_dict)["start_value"], float(params_dict["value"]))

    @patch("converter.currency_converter.logger")
    def test_count_result_value(self, logger):
        for params in wrong_params_for_count:
            with self.subTest(msg=f"test with {params}"):
                self.assertTrue(isinstance(self.obj._count_result_value(*params), str))



if __name__ == "__main__":
    main()
