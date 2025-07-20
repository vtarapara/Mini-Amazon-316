#!/bin/bash

mypath=`realpath $0`
mybase=`dirname $mypath`
cd $mybase

# SECRET=`` removed 50-character randomly generated secret
echo "FLASK_APP=amazon.py
FLASK_DEBUG=True
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=8080
SECRET_KEY='$SECRET'
DB_NAME=amazon
DB_USER=${PGUSER}
DB_PORT=${PGPORT}
DB_HOST=${PGHOST}
DB_PASSWORD=${PGPASSWORD}" > .flaskenv

poetry config virtualenvs.in-project true
poetry install
db/setup.sh
