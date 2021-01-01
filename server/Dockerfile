FROM python:3.8-alpine
LABEL maintainer="parkyes90"

RUN apk add --update --no-cache postgresql-client jpeg-dev \
    libffi-dev musl-dev make python3-dev libevent-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock -d --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . .

