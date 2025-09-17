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
    
    # Show packages to install
    packages_to_install = []
    if use_drf == "y":
        packages_to_install.append("djangorestframework")
    if use_cache == "y":
        packages_to_install.append("django-redis")
    if use_celery == "y":
        if celery_broker == "redis":
            packages_to_install.append("celery[redis]")
        else:
            packages_to_install.append("celery")
    
    if packages_to_install:
        print(f"\n📦 Additional packages to install:")
        for package in packages_to_install:
            print(f"  • {package}")
    
    print(f"\n🚀 Next steps:")
    print(f"1. cd {project_slug}")
    print("2. pip install -r requirements.txt")
    if packages_to_install:
        print(f"3. pip install {' '.join(packages_to_install)}")
    print("4. python manage.py migrate")
    print("5. python manage.py createsuperuser")
    print("6. python manage.py runserver")
    {% if cookiecutter.use_celery == "y" %}
    print("7. celery -A core worker -l info  # (in another terminal)")
    {% endif %}
    
    print(f"\n✨ Your Django project is ready to go!")

if __name__ == "__main__":
    main()
