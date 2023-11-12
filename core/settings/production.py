from .base import *  # noqa

DEBUG = False

# ALLOWED_HOSTS = ['lordstormrage.pythonanywhere.com', 'localhost', '45.89.190.14']
ALLOWED_HOSTS = ['*']
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
