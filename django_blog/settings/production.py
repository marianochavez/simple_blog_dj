from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogch.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'dfsi1bdnfhmbbk',

        'USER': 'fzywmdjcyamtnf',

        'PASSWORD': 'c01f2e931fea5df32ac2cf5a7ea7f1e024752495cb23373122e8f62d8bbf4022',

        'HOST': 'ec2-54-167-168-52.compute-1.amazonaws.com',

        'PORT': 5432,

    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
