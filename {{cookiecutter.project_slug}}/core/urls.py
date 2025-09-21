"""
URL configuration for {{ cookiecutter.project_slug }} project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
{% if cookiecutter.use_drf == "y" and cookiecutter.use_jwt == "y" %}
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
{% endif %}
{% if cookiecutter.use_api_docs == "y" and cookiecutter.use_drf == "y" %}
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
{% endif %}

urlpatterns = [
    path('admin/', admin.site.urls),
    {% if cookiecutter.use_drf == "y" %}
    path('api-auth/', include('rest_framework.urls')),
    {% if cookiecutter.use_jwt == "y" %}
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    {% endif %}
    {% if cookiecutter.use_api_docs == "y" %}
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    {% endif %}
    {% endif %}
    {% if cookiecutter.use_custom_user == "y" %}
    path('', include('user.urls')),
    {% endif %}
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
