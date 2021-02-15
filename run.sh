#!/bin/bash

docker volume create --name=converter_app

docker-compose up -d --build
