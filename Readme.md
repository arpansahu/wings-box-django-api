
# Django React Blog API

This project is implementation for the following topics related to technologies used with Django

-Implemented Complete Auth Using Django Custom Auth Model.
    
1. Implemented custom Auth Model and its Manager
2. Implemented custom error View for customizing Templates
3. Login. SingUp, Logout, Account Views Implemented
4. In built views of PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetView, PasswordResetCompleteView
5. Build Custom Templates for These Inbuilt Views

-Implemented Social Login using drf-social-oauth2, which combines normal auth and social auth 

1. you can integrate different social accounts with an already created normal account using simple email registration
2. manage your account and profile

-Implemented Crud Operations with Django Rest Framework 

1. read operation for all posts using DRF
2. Build API for updating posting a json file

-Deployed on Heroku

1. Used Heroku Postgres 
2. Used AWS S3 Bucket for static and media files

## What is Celery ?
Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation but supports scheduling as well.

Why is this useful?

1. Think of all the times you have had to run a certain task in the future. Perhaps you needed to access an API every hour. Or maybe you needed to send a batch of emails at the end of the day. Large or small, Celery makes scheduling such periodic tasks easy.
2. You never want end users to have to wait unnecessarily for pages to load or actions to complete. If a long process is part of your application’s workflow, you can use Celery to execute that process in the background, as resources become available, so that your application can continue to respond to client requests. This keeps the task out of the application’s context.

Working:
1. Celery requires message broker to store messages received from task generators or producers. For reading information of messages in task
  serialization is required which can be in json/pickle/yaml/msgpack it can be in compressed form as zlib, bzip2 or a cryptographic message.
2. A celery system consists of multiple workers and brokers, giving way to high availability and horizontal scaling.
3. When a celery worker is started using command ```celery -A [core(project name)].celery worker -l info```, a supervisor is started.
4. Which spawns child processes or threads and deals with all the bookkeeping stuff. The child processes or threads execute the actual task.
  This child process are also known as execution pool. By default, no of child process worker can spawn is equal to the no of CPU cores.
5. The size of execution pool determines the number of tasks your celery worker can process
   1. Worker ----- Pool ----- Concurrency 
   2. When you start a celery worker, you specify the pool, concurrency, autoscale etc. in the command 
   3. Pool - Decides who will actually perform the task -thread, child process, worker itself or else. 
   4. Concurrency: will decide the size of pool
   5. autoscale: to dynamically resize the pool based on load. The autoscaler adds more pool processes when there is work
     to do, and starts removing processes when the workload is low.
   6. ```celery -A <project>.celery worker --pool=preform --concurrency=5 --autoscale=10 3 -l info ``` 
    this command states to start a worker with 5 child processes which can be auto-scaled upto 10 and can be decreased upto 3.
6. Type of Pools: 
    1. prefork (multiprocessing) (default):
       1. Use this when CPU bound task
       2. By passes GIL (Global Interpreter Lock)
       3. The number of available cores limits the number of concurrent processes.
       4. That's why Celery defaults concurrency to no of CPU cores available.
       5. Command: ```celery A -<project>.celery worker -l info```
    2. solo (Neither threaded nor process-based)
        1. Celery don't support windows, so you can use this pool of running celery on Windows
        2. It doesn't create pool as it runs solo.
        3. Contradicts the principle that the worker itself does not process any tasks
        4. The solo pool runs inside the worker process.
        5. This makes the solo worker fast, But it also blocks the worker while it executes tasks.
        6. In this concurrency doesn't make any sense.
        7. Command ```celery A -<project>.celery worker --pool=solo -l info```
    3. threads (multi threading)
        1. due to GIL in CPython, it restricts to single thread so can't achieve real multithreading
        2. Not much official support
        3. Uses threading module of python
        4. Command ```celery A -<project>.celery worker --pool=threads -l info```
    4. gevent/eventlet (Green Threads)
       1. Uses Green thread which are user level threads so can be manipulated at code level 
       2. This can be used to get a thousand of HTTP get request to fetch from external REST APIs.
       3. The bottleneck is waiting for I/O operation to finish and not CPU.
       4. There are implementation differences between the eventlet and gevent packages
       5. Command ```celery A -<project>.celery worker --pool=[gevent/eventlet] worker -l info```
    5. by default ```celery A -<project>.celery worker -l info``` uses pool-prefork and concurrency -no of cores
    6. Difference between greenlets and threads -
       1. Python's threading library makes use of the system's native OS to schedule threads. This general-purpose scheduler is not always very efficient. 
       2. It makes use of Python's global interpreter lock to make sure shared data structures are accessed by only one thread at a time to avoid race conditions.
          CPython Interpreter, GIL, OS Greenlets emulate multi-threaded environments without relying on any native operating system capabilities.
          Greenlets are managed in application space and not in kernel space. In greenlets, no scheduler pre-emptively switching between your threads
          at any given moment. 
       3. Instead, your greenlets voluntarily or explicitly give up control to one another at specified points in your code. 
       4. Thus more scalable and efficient. Less RAM required.
       
## What is Redis ?
    
Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. 
The most common Redis use cases are session cache, full-page cache, queues, leaderboards and counting, publish-subscribe, and much more. in this case, we will use Redis as a message broker.


## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Jquery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![Celery](https://img.shields.io/badge/celery-%2337814A.svg?&style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/index.html)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

## Demo

Backend Available at: https://files-box-django-api.herokuapp.com/

FrontEnd Available at: https://wings-box-react.herokuapp.com/

Note: Both the projects are running on Free dynos of Heroku so Please makesure before accessing Frontend Project 
    awake the Backend by visiting the backend link


admin login details:--
email: admin@arpansahu.me
password: showmecode
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installing Pre requisites
```bash
  pip install -r requirements.txt
```

Create .env File
```bash
  add variables mentioned in .env.example
```

Making Migrations and Migrating them.
```bash
  python manage.py makemigrations
  python manage.py migrate
```

Creating Super User
```bash
  python manage.py createsuperuser
```

Installing Redis On Local (For ubuntu) for other Os Please refer to their website https://redis.io/
```bash
  curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
  sudo apt-get update
  sudo apt-get install redis
  sudo systemctl restart redis.service
```
to check if its running or not
```
  sudo systemctl status redis
```
--------------------------

Use these CELERY settings

``` 
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
```

---

Creating Celery App - create a file named celery.py in project directory.
``` 


import os

from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

redis_url = config("REDISCLOUD_URL")

app = Celery('core', broker=redis_url, backend=redis_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

```


Run Server
```bash
  python manage.py runserver
```

## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  heroku config:set GITHUB_USERNAME=joesmith

```
Configuring Django App for Heroku

Install whitenoise 
```
pip install whitenoise 
```

Include it in Middlewares.
```
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

Create Procfile and include this code snippet in it.
```
release: python manage.py migrate
web: daphne core.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A core.celery worker -l info
```

In the above Procfile there are two workers required for web, celery and celery beat, since heroku free
plan only allows upto 2 free dynos we can easily run web and celery worker

Comment down Database setting and install or use a local/prod settings file or comment down

``` 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }
```
```
pip install dj-database-url
```

and add these lines below the commented Database settings
``` 
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}
```

Change CELERY_BROKER_URL from 
``` 
CELERY_BROKER_URL = 'redis://localhost:6379'
```
to
```
CELERY_BROKER_URL=config("REDISCLOUD_URL")
```

## Tech Stack

**Client:** HTML, Jinja, CSS, BootStrap, Jquery

**Server:** Django, Django Rest Framework, Gunicorn, GraphQL, Heroku


## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  add all the env variables used from app setting page on heroku app dashboard.

```
Configuring Django App for Heroku
```
    install whitenoise : pip install whitenoise 
    include it in included_apps=[]
    add whitenoise middleware
    add: procfile
    add: release-task.sh for running mutilple commands in run: section of procfile
    make relase-task.sh executable : chmod +x release-tasks.sh 
```
## Documentation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![Celery](https://img.shields.io/badge/celery-%2337814A.svg?&style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/index.html)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

REDISCLOUD_URL=

SECRET_KEY=

DEBUG=

ALLOWED_HOSTS=

DATABASE_URL=

MAIL_JET_API_KEY=

MAIL_JET_API_SECRET=

MAILJET_EMAIL=

DOMAIN=

PROTOCOL=

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_STORAGE_BUCKET_NAME=