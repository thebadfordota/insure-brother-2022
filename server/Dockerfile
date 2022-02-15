# pull official base image
FROM python:3.8.3-alpine
# set work directory
#WORKDIR /usr/src/app
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