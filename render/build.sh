#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


pip install -r requirements.txt
# python manage.py collectstatic --noinput
python manage.py migrate