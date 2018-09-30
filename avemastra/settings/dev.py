from .base import *

ALLOWED_HOSTS = []

MIDDLEWARE += [
    'livereload.middleware.LiveReloadScript',
]

INSTALLED_APPS += [
    'livereload',
]
