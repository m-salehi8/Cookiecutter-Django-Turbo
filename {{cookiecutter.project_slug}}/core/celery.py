{% if cookiecutter.use_celery == "y" %}
"""
Celery configuration for {{ cookiecutter.project_slug }} project.

This module contains the Celery application instance and configuration.
"""

import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('{{ cookiecutter.project_slug }}')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """Debug task to test Celery functionality."""
    print(f'Request: {self.request!r}')
    return 'Celery is working!'


# Celery Beat configuration for periodic tasks
app.conf.beat_schedule = {
    'debug-task-every-30-seconds': {
        'task': 'core.celery.debug_task',
        'schedule': 30.0,
    },
}
app.conf.timezone = 'UTC'
{% endif %}
