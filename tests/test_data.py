from io import BytesIO as IO


wrong_syntax_params = [
    ["test=test", "to-USD", "value=20.2"],
    ["from==RUB", "to=USD", "value=10"],
    ["from-RUB", "to=RUB", "value-=9"],
    ["from=RUB", "to&USD", "value=4"]
]

wrong_length_params = [
    ["from=RUB", "to=USD", "test", "value"],
    ["from=RUB", "to=USD"]
]

wrong_name_params = [
    ["test=test", "to=USD", "value=20.2"],
    ["from=RUB", "t=UI", "value=20.2"],
    ["from=RUB", "to=USD", "vale=20.2"],
]

wrong_values_params = [
    {"from": "RUB", "to": "RUB", "value": "10,0"},
    {"from": "USD", "to": "test", "value": False},
    {"from": True, "to": "RUB", "value": "test"}
]

wrong_params_for_count = [
    ("10", "test"),
    ("test", "USD > RUB")
]

right_values_params = [
    {"from": "RUB", "to": "USD", "value": "100"},
    {"from": "USD", "to": "RUB", "value": "10.0"},
]

right_params = ["from=RUB", "to=USD", "value=20.2"]


class MockSocket(object):
    def getsockname(self):
        return ('sockname',)


class MockRequest(object):
    _sock = MockSocket()

    def __init__(self, path):
        self._path = path

    def makefile(self, *args, **kwargs):
        if args[0] == 'rb':
            return IO(b"GET %s HTTP/1.0" % self._path)
        elif args[0] == 'wb':
            return IO(b'')
        else:
            raise ValueError("Unknown file type to make", args, kwargs)

    def sendall(self, *args, **kwargs):
        pass
