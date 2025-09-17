# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
{% if cookiecutter.use_celery == "y" %}
from .celery import app as celery_app

__all__ = ('celery_app',)
{% endif %}
