import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
         'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
         'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
         'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
         'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda',
        'USER': 'postgres',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tienda',
        'USER': 'root',
        'PASSWORD': '14CEB00F',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')