from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = ['lordstormrage.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = [
    '',
    '',
]

CORS_ALLOW_CREDENTIALS = True

SITE_ID = 2