release: python manage.py migrate
web: gunicorn core.wsgi
celery: celery -A core.celery worker -l info