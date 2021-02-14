""" Module implemented validation params list from request query """


class ValidationError(Exception):
    pass


def validate_params_list(params: list) -> list:

    """
    Function checking that params allow this template :
    params = ['from'=<some_currency>, 'to'=<some_currency>]
    """

    if len(params) != 2:
        raise ValidationError (f"It needs to be exactly two params in query, given {len(params)}")

    if len(params[0].split("=")) != 2 or len(params[1].split("=")) != 2:
        raise ValidationError (f"Sintax error in params! {params}")

    if params[0].split("=")[0] != "from" or params[1].split("=")[0] != "to":
        raise ValidationError (f"Params need to be 'from' and 'to', given: {params}")

    return params
