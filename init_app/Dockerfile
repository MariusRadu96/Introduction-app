FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1


ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .