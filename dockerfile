FROM python:3.7.9-slim

WORKDIR /api

RUN apt-get update
RUN apt-get install -y g++ libffi-dev openssl libxml2-dev libxslt-dev

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

COPY . /api

ENV TZ America/Sao_Paulo

