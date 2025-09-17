from django.urls import path
from . import views
{% if cookiecutter.use_drf == "y" and cookiecutter.use_custom_user == "y" %}
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
{% endif %}

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
{% if cookiecutter.use_drf == "y" and cookiecutter.use_custom_user == "y" %}
]

urlpatterns += router.urls
{% else %}
]
{% endif %}
