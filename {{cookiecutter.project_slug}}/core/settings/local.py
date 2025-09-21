"""
Django local development settings for {{ cookiecutter.project_slug }} project.
"""

from .base import *

# Override base settings for local development
DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ['*']

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging configuration for development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        '{{ cookiecutter.project_slug }}': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
