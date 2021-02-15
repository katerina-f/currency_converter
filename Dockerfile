FROM python:3.8
WORKDIR /converter
COPY . .

CMD ["python", "runserver.py"]
