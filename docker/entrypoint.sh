#!/bin/sh

# Install necessary packages and Python dependencies
apk add --no-cache python3 py3-pip
pip3 install --upgrade pip
pip3 install openai==0.26.0
apk add --no-cache build-base python3-dev
python3 -m pip install --upgrade openai

rm cybermillionaire/__init__.py
touch cybermillionaire/__init__.py

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn cybermillionaire.wsgi:application --bind 0.0.0.0:8000
