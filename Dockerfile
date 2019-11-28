FROM python:3.7.5-alpine3.9

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN apk add --no-cache --virtual .build-deps \
    bash \
    build-base \
    curl \
    gcc \
    libffi-dev \
    linux-headers \
    openssl \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    && pip install pip --upgrade

WORKDIR /code

COPY . /code

RUN pip install -r /code/requirements.txt --no-cache-dir