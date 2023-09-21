FROM python:3.9-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password drf-user

USER drf-user
