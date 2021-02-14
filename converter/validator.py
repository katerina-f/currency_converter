""" Module implemented validation params list from request query """
from typing import List


class ValidationError(Exception):
    """ Custom exception class for validation errors """


def validate_params_list(params: List[str]) -> List[str]:

    """
    Function checking that params match this template :
    params = ['from'=<some_currency>, 'to'=<some_currency>]
    """

    if len(params) != 3:
        raise ValidationError (f"It needs to be exactly three params in query, given {len(params)}")

    if any([len(param.split("=")) != 2 for param in params]):
        raise ValidationError (f"Syntax error in params! {params}")

    if params[0].split("=")[0] != "from" or \
    params[1].split("=")[0] != "to" or \
    params[2].split("=")[0] != "value":
        raise ValidationError (f"Params need to be 'from', 'to' and 'value', given: {params}")

    return params
