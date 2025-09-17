# 🚀 CookieCutter Django Turbo

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://djangoproject.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CookieCutter](https://img.shields.io/badge/CookieCutter-Template-red.svg)](https://cookiecutter.readthedocs.io)

> **The ultimate Django project template** - Fast, modern, and feature-rich Django applications in seconds! ⚡

A comprehensive, production-ready Django project template with configurable features including custom User models, multiple database options, Redis caching, Celery task queues, and Django REST Framework.

## ✨ Features

### 🗄️ **Database Options**
- **PostgreSQL** - Full-featured with psycopg2
- **MySQL** - Enterprise-ready with mysqlclient  
- **SQLite** - Lightweight for development

### 👤 **Flexible Authentication**
- **Custom User Model** - Optional with configurable login field
- **Email Login** - Email as unique identifier
- **Phone Login** - Phone number authentication
- **Username Login** - Traditional Django default

### 🚀 **Modern Stack**
- **Django REST Framework** - Powerful API framework
- **Redis Caching** - High-performance caching
- **Celery** - Background task processing
- **Multiple Brokers** - Redis or RabbitMQ support

### 🛠️ **Developer Experience**
- **Production Ready** - Gunicorn, WhiteNoise, logging
- **Testing Setup** - pytest configuration included
- **Code Quality** - Black, flake8, isort pre-configured
- **Beautiful UI** - Modern home page template

## 🚀 Quick Start

### 1. Install CookieCutter
```bash
pip install cookiecutter
```

### 2. Generate Your Project
```bash
cookiecutter https://github.com/your-username/ookiecutter-django-turbo
```

### 3. Follow the Interactive Prompts
```
project_name [My Django Project]: My Awesome App
project_slug [my_awesome_app]: 
Select database:
1 - postgres
2 - sqlite  
3 - mysql
Choose from [1/2/3] (1): 1
# ... more configuration options
```

### 4. Set Up Your Project
```bash
cd my_awesome_app
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**🎉 That's it!** Your Django app is running at `http://127.0.0.1:8000`

## 📁 Project Structure

```
my_awesome_app/
├── 📄 manage.py
├── 📄 requirements.txt
├── 📁 core/                    # Django settings & config
│   ├── __init__.py
│   ├── settings.py            # Dynamic configuration
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py              # Celery config (if enabled)
├── 📁 user/                   # Custom user app (if enabled)
│   ├── models.py              # Custom User model
│   ├── views.py               # API views (if DRF enabled)
│   ├── admin.py               # Custom admin
│   ├── serializers.py         # DRF serializers
│   └── templates/
└── 📁 logs/                   # Auto-created logging
```

## ⚙️ Configuration Options

| Feature | Options | Description |
|---------|---------|-------------|
| **Database** | PostgreSQL, MySQL, SQLite | Choose your data store |
| **User Model** | Default, Email, Phone | Flexible authentication |
| **API Framework** | Django REST Framework | Optional API endpoints |
| **Caching** | Redis | High-performance caching |
| **Task Queue** | Celery + Redis/RabbitMQ | Background processing |

## 🛠️ Development

### Start Development Server
```bash
python manage.py runserver
```

### Run Background Tasks (if Celery enabled)
```bash
celery -A core worker -l info
```

### Run Tests
```bash
pytest
```

### Code Formatting
```bash
black .
flake8
isort .
```

## 🚀 Production Deployment

The template includes production-ready configurations:

- **WSGI Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Logging**: Comprehensive logging setup
- **Security**: Production security settings
- **Monitoring**: Health checks and metrics

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [CookieCutter](https://cookiecutter.readthedocs.io)
- Powered by [Django](https://djangoproject.com)
- Inspired by the Django community

---

**Made with ❤️ for the Django community**