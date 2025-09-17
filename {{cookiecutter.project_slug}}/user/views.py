from django.shortcuts import render
from django.contrib.auth.decorators import login_required
{% if cookiecutter.use_drf == "y" %}
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
{% if cookiecutter.use_custom_user == "y" %}
from .models import User
from .serializers import UserSerializer
{% endif %}
{% endif %}


def home(request):
    """Home page view."""
    return render(request, 'user/home.html')


{% if cookiecutter.use_drf == "y" and cookiecutter.use_custom_user == "y" %}
class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user information."""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
{% endif %}
