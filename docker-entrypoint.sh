#!/bin/sh

if [ "1" = "1" ]
then

  echo "RUN CUSTOM COMMAND"

  python manage.py create_users -u
  python manage.py create_users -a
  python manage.py create_users -m
  python manage.py create_users -a -n compaspro -e compaspro@compas.ru -p compaspro
  python manage.py create_users




fi

exec "$@"