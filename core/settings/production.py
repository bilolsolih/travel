from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['lordstormrage.pythonanywhere.com', 'localhost']

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
