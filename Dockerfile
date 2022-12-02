FROM python:3.8

COPY ./requirements /requirements
RUN pip install -r requirements/base.in
RUN pip install -r requirements/dev.in
RUN pip install -r requirements/test.in

RUN apt-get update

WORKDIR /app
COPY . /app/
