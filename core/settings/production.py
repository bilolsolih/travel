from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = [
    'bilolsolih.pythonanywhere.com',
    'localhost',
    '45.89.190.14',
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

CORS_ALLOW_CREDENTIALS = True

SITE_ID = 2
