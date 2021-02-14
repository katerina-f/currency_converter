# internal modules
from unittest import TestCase, main

# project modules
from converter.validator import validate_params_list, ValidationError

from .test_data import wrong_length_params, \
                       wrong_name_params, \
                       wrong_syntax_params, \
                       right_params


class TestValidator(TestCase):

    def test_validate_params_list_length(self):
        for params_list in wrong_length_params:
            with self.subTest(msg=f"test with {params_list}"):
                with self.assertRaises(ValidationError) as err:
                    validate_params_list(params_list)

                self.assertEqual(
                    f"It needs to be exactly three params in query, given {len(params_list)}",
                    str(err.exception)
                )

    def test_validate_params_list_names(self):
        for params_list in wrong_name_params:
            with self.subTest(msg=f"test with {params_list}"):
                with self.assertRaises(ValidationError) as err:
                    validate_params_list(params_list)

                self.assertEqual(f"Params need to be 'from', 'to' and 'value', given: {params_list}",
                                 str(err.exception))

    def test_validate_params_list_syntax(self):
        for params_list in wrong_syntax_params:
            with self.subTest(msg=f"test with {params_list}"):
                with self.assertRaises(ValidationError) as err:
                    validate_params_list(params_list)

                self.assertEqual(f"Syntax error in params! {params_list}",
                                 str(err.exception))

    def test_passing_validation(self):
        self.assertEqual(right_params, validate_params_list(right_params))


if __name__ == "__main__":
    main()
