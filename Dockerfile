FROM python:3.7.3-alpine3.9

LABEL author=xiaolong@caicloud.io

COPY requirements.txt .
RUN apk add python3 git --update \
  && apk add --virtual .build-deps \
  python3-dev musl-dev gcc libffi-dev openssl-dev \
  libxml2-dev \
  && pip3 install --upgrade pip \
  && pip3 install  --no-cache-dir -r ./requirements.txt \
  && apk del .build-deps
RUN pip install kubernetes ptvsd

WORKDIR /errbot


