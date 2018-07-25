FROM python:3.6-slim

WORKDIR /app

ADD . /

RUN pip install --trusted-host pypi.python.org -r requirements.txt