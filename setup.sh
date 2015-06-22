#! /bin/bash
source django/bin/activate
python manage.py test
python manage.py makemigrations
python manage.py migrate
rm -rf static_files
python manage.py collectstatic --noinput
