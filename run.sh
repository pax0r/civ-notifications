#!/usr/bin/env sh
# script to run application in Docker container
# it will run migrate on start

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
uwsgi --ini uwsgi.ini