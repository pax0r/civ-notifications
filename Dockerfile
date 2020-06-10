FROM python:3.8-slim-buster
EXPOSE 3031

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY . .
RUN pip3 install --no-cache-dir -U pip setuptools wheel uwsgi
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
CMD ["./run.sh"]