#!/bin/sh

while true; do
    python manage.py migrate
    if [ $? -eq 0 ]; then
        break
    else
        echo 'Migrate command failed, retrying in 5 secs...'
    fi
    sleep 5
done
exec gunicorn -b :8000 bloggy.wsgi