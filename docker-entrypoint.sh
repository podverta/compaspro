#!/bin/sh

if [ "1" = "1" ]
then
  echo "migrate"

  python manage.py makemigrations user_selection
  python manage.py migrate


  echo "run command"

  python manage.py create_users -u
  python manage.py create_users -a
  python manage.py create_users -m

fi
exec "$@"

