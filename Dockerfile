# syntax = docker/dockerfile:experimental
FROM python:3.8-slim-buster
EXPOSE 3031

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY . .
RUN  --mount=type=cache,target=/root/.cache/pip pip3 install -U pip setuptools wheel uwsgi
RUN  --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt
RUN chmod +x run.sh
CMD ["./run.sh"]