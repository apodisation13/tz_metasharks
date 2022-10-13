#!/usr/bin/env bash

set -euxo pipefail

sleep 10s

python manage.py migrate --no-input

python manage.py collectstatic --no-input

gunicorn config.wsgi --bind 0.0.0.0
