#!/usr/bin/env python3
"""
Post-generation hook for oookiecutter-django-turbo
This hook runs after the project is generated.
"""

import os
import sys

def main():
    """Post-generation setup and instructions."""
    # Get the project context
    project_slug = "{{ cookiecutter.project_slug }}"
    use_drf = "{{ cookiecutter.use_drf }}"
    use_cache = "{{ cookiecutter.use_cache }}"
    use_celery = "{{ cookiecutter.use_celery }}"
    celery_broker = "{{ cookiecutter.celery_broker }}"
    use_docker = "{{ cookiecutter.use_docker }}"
    use_jwt = "{{ cookiecutter.use_jwt }}"
    use_api_docs = "{{ cookiecutter.use_api_docs }}"
    use_precommit = "{{ cookiecutter.use_precommit }}"
    
    print(f"\n🎉 Django project '{project_slug}' generated successfully!")
    print(f"📁 Project location: {os.path.join(os.getcwd(), project_slug)}")
    
    # Show configuration summary
    print("\n📋 Project Configuration:")
    print(f"  • Database: {{ cookiecutter.database|title }}")
    print(f"  • Custom User Model: {{ cookiecutter.use_custom_user|title }}")
    {% if cookiecutter.use_custom_user == "y" %}
    print(f"  • User Login Field: {{ cookiecutter.user_login_field }}")
    {% endif %}
    print(f"  • Django REST Framework: {{ cookiecutter.use_drf|title }}")
    print(f"  • Redis Caching: {{ cookiecutter.use_cache|title }}")
    print(f"  • Celery: {{ cookiecutter.use_celery|title }}")
    {% if cookiecutter.use_celery == "y" %}
    print(f"  • Celery Broker: {{ cookiecutter.celery_broker }}")
    {% endif %}
    print(f"  • Docker Support: {{ cookiecutter.use_docker|title }}")
    {% if cookiecutter.use_drf == "y" %}
    print(f"  • JWT Authentication: {{ cookiecutter.use_jwt|title }}")
    print(f"  • API Documentation: {{ cookiecutter.use_api_docs|title }}")
    {% endif %}
    print(f"  • Pre-commit Hooks: {{ cookiecutter.use_precommit|title }}")
    
    # Show packages to install
    packages_to_install = []
    if use_drf == "y":
        packages_to_install.append("djangorestframework")
        if use_jwt == "y":
            packages_to_install.append("djangorestframework-simplejwt")
        if use_api_docs == "y":
            packages_to_install.append("drf-spectacular")
    if use_cache == "y":
        packages_to_install.append("django-redis")
    if use_celery == "y":
        if celery_broker == "redis":
            packages_to_install.append("celery[redis]")
        else:
            packages_to_install.append("celery")
    if use_precommit == "y":
        packages_to_install.append("pre-commit")
    
    if packages_to_install:
        print(f"\n📦 Additional packages to install:")
        for package in packages_to_install:
            print(f"  • {package}")
    
    print(f"\n🚀 Next steps:")
    print(f"1. cd {project_slug}")
    
    # Environment setup
    {% if cookiecutter.use_docker == "y" %}
    print("2a. Copy .env.example to .env and configure your environment variables")
    print("    OR copy .env.docker.example to .env for Docker-specific configuration")
    {% else %}
    print("2. Copy .env.example to .env and configure your environment variables")
    {% endif %}
    
    {% if cookiecutter.use_docker == "y" %}
    print("2b. pip install -r requirements.txt")
    {% else %}
    print("3. pip install -r requirements.txt")
    {% endif %}
    
    if packages_to_install:
        {% if cookiecutter.use_docker == "y" %}
        print(f"2c. pip install {' '.join(packages_to_install)}")
        {% else %}
        print(f"4. pip install {' '.join(packages_to_install)}")
        {% endif %}
    
    {% if cookiecutter.use_precommit == "y" %}
    {% if cookiecutter.use_docker == "y" %}
    print("2d. pre-commit install")
    {% else %}
    print("5. pre-commit install")
    {% endif %}
    {% endif %}
    
    {% if cookiecutter.use_docker == "y" %}
    print("3. python manage.py migrate")
    print("4. python manage.py createsuperuser")
    print("5. python manage.py runserver")
    {% if cookiecutter.use_celery == "y" %}
    print("6. celery -A core worker -l info  # (in another terminal)")
    {% endif %}
    print("\n🐳 Docker users:")
    print("  • cp .env.docker.example .env  # Use Docker-specific environment variables")
    print("  • docker-compose up --build")
    print("  • docker-compose exec web python manage.py migrate")
    print("  • docker-compose exec web python manage.py createsuperuser")
    print("  • Access your app at: http://localhost:8000")
    {% else %}
    print("6. python manage.py migrate")
    print("7. python manage.py createsuperuser")
    print("8. python manage.py runserver")
    {% if cookiecutter.use_celery == "y" %}
    print("9. celery -A core worker -l info  # (in another terminal)")
    {% endif %}
    {% endif %}
    
    {% if cookiecutter.use_api_docs == "y" and cookiecutter.use_drf == "y" %}
    print("\n📚 API Documentation:")
    print("  • Swagger UI: http://localhost:8000/api/schema/swagger-ui/")
    print("  • ReDoc: http://localhost:8000/api/schema/redoc/")
    {% endif %}
    
    print(f"\n✨ Your Django project is ready to go!")

if __name__ == "__main__":
    main()
