

wrong_syntax_params = [
    ["test=test", "to-USD"],
    ["from==RUB", "to=USD"],
    ["from-RUB", "to=RUB"],
    ["from=RUB", "to&USD"]
]

wrong_length_params = [
    ["from=RUB", "to=USD", "test"],
    ["from=RUB"]
]

wrong_name_params = [
    ["test=test", "to=USD"],
    ["from=RUB", "t=UI"]
]

right_params = ["from=RUB", "to=USD"]
