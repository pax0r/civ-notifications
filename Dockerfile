FROM alpine:3.7
EXPOSE 3031

WORKDIR /usr/src/app

RUN apk add --no-cache \
        uwsgi-python3 \
        python3
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
               "--uid", "uwsgi", \
               "--plugins", "python3", \
               "--protocol", "uwsgi", \
               "--wsgi", "civ_notifcations.wsgi:application" ]