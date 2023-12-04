# shellcheck disable=SC2164
cd eduplatform; python manage.py migrate; python manage.py runserver 0.0.0.0:8000;
