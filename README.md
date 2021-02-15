# Currency Converter

Application for converting currency

### Instalation

To install and run the code in the docker containers,
make script
```
run.sh
```
executable
```
chmod +x ./run.sh
```

This script will start building the application.

and run it in the project root
```
./run.sh
```

#### Tests

To running tests execute
```
python -m unittest -v tests/*.py
```
in the project root

## Examples for API

#### GET

Right request
```
http://0.0.0.0:8080/?from=RUB&to=USD&value=100
```
Returns result with converted value

```
{"converting_type": "RUB > USD", "start_value": 100.0, "result_value": 1.37}
```

If request is wrong, returns error message
```
http://0.0.0.0:8080/?from=RUB&to=USD&value=test
```
returns error message
```
Invalid type of currency value! could not convert string to float: 'test'
```

## Authors

* **Katerina Frolova** - *Initial work* - [katerina-f](https://github.com/katerina-f)
