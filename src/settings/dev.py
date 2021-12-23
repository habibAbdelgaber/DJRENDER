from .base import *
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['hello-world-0ikz.onrender.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
