# pull official base image
FROM python:3.10.2-alpine3.15
# set work directory
WORKDIR /code
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev zlib-dev jpeg-dev  musl-dev
# install dependencies
RUN pip install --upgrade pip
#COPY ./requirements.txt .
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# copy project
COPY . /code/