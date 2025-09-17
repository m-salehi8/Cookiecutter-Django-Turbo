{% if cookiecutter.use_custom_user == "y" %}
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for {{ cookiecutter.project_slug }}.
    
    {% if cookiecutter.user_login_field == "email" %}
    Uses email as the unique identifier instead of username.
    {% elif cookiecutter.user_login_field == "phone" %}
    Uses phone number as the unique identifier instead of username.
    {% else %}
    Uses the default Django username field.
    {% endif %}
    """
    
    {% if cookiecutter.user_login_field == "email" %}
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    {% elif cookiecutter.user_login_field == "phone" %}
    phone = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'email']
    {% endif %}
    
    def __str__(self):
        {% if cookiecutter.user_login_field == "email" %}
        return self.email
        {% elif cookiecutter.user_login_field == "phone" %}
        return self.phone
        {% else %}
        return self.username
        {% endif %}
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
{% else %}
# Using Django's default User model
from django.contrib.auth.models import User
{% endif %}
