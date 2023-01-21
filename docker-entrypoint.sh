#!/bin/sh

if [ "1" = "1" ]
then
  echo "migrate"
  echo "RUN MIGRATIONS"
  python manage.py makemigrations user_selection
  python manage.py migrate


  echo "RUN CUSTOM COMMAND"

  python manage.py create_users -u
  python manage.py create_users -a
  python manage.py create_users -m

fi

exec "$@"