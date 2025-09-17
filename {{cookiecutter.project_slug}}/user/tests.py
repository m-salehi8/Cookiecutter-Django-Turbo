from django.test import TestCase
from django.contrib.auth import get_user_model
{% if cookiecutter.use_custom_user == "y" %}
from .models import User
{% endif %}

{% if cookiecutter.use_custom_user == "y" %}
class UserModelTest(TestCase):
    """Test cases for User model."""
    
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        {% if cookiecutter.user_login_field == "phone" %}
        self.user_data['phone'] = '+1234567890'
        {% endif %}
    
    def test_user_creation(self):
        """Test user creation."""
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        {% if cookiecutter.user_login_field == "phone" %}
        self.assertEqual(user.phone, '+1234567890')
        {% endif %}
    
    def test_user_str_representation(self):
        """Test user string representation."""
        user = User.objects.create_user(**self.user_data)
        {% if cookiecutter.user_login_field == "email" %}
        self.assertEqual(str(user), 'test@example.com')
        {% elif cookiecutter.user_login_field == "phone" %}
        self.assertEqual(str(user), '+1234567890')
        {% else %}
        self.assertEqual(str(user), 'testuser')
        {% endif %}
    
    def test_user_username_field(self):
        """Test USERNAME_FIELD configuration."""
        {% if cookiecutter.user_login_field == "email" %}
        self.assertEqual(User.USERNAME_FIELD, 'email')
        {% elif cookiecutter.user_login_field == "phone" %}
        self.assertEqual(User.USERNAME_FIELD, 'phone')
        {% else %}
        self.assertEqual(User.USERNAME_FIELD, 'username')
        {% endif %}
{% else %}
class UserTest(TestCase):
    """Test cases for default User model."""
    
    def test_user_creation(self):
        """Test user creation with default User model."""
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
{% endif %}
