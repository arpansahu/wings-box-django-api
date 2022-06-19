import os
from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
redis_url = config("REDISCLOUD_URL")
app = Celery('core', broker=redis_url, backend=redis_url)

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
