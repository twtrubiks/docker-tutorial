#!/bin/sh
echo 'Run migration'
python3 manage.py makemigrations musics
python3 manage.py migrate
echo 'Create Super User'
python3 manage.py createsuperuser --noinput || echo "Super user already created"
exec "$@"
