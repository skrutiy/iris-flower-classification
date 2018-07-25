FROM python:2.7-slim

WORKDIR /app

ADD . /

RUN pip install --trusted-host pypi.python.org -r requirements.txt