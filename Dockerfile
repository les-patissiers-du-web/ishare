FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

VOLUME /app

RUN apk update && apk upgrade
RUN apk add alpine-sdk openssl-dev python-dev

RUN python setup.py install

RUN apk del build-dependencies alpine-sdk openssl-dev python-dev
