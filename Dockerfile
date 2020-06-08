FROM alpine:3.7
EXPOSE 3031

WORKDIR /usr/src/app

RUN apk add --no-cache \
        uwsgi-python3 \
        python3 \
        python3-dev \
        postgresql-dev \
        alpine-sdk

COPY . .
RUN pip3 install --no-cache-dir -U pip setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]