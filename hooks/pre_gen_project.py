#!/usr/bin/env python3
"""
Pre-generation hook for oookiecutter-django-turbo
This hook runs before the project is generated.
"""

import sys
import os

def main():
    """Pre-generation validation and setup."""
    # Get the project context
    project_name = "{{ cookiecutter.project_name }}"
    project_slug = "{{ cookiecutter.project_slug }}"
    use_custom_user = "{{ cookiecutter.use_custom_user }}"
    user_login_field = "{{ cookiecutter.user_login_field }}"
    use_celery = "{{ cookiecutter.use_celery }}"
    celery_broker = "{{ cookiecutter.celery_broker }}"
    
    # Validate project name
    if not project_name or not project_name.strip():
        print("ERROR: Project name cannot be empty!")
        sys.exit(1)
    
    # Validate project slug
    if not project_slug or not project_slug.strip():
        print("ERROR: Project slug cannot be empty!")
        sys.exit(1)
    
    # Validate custom user configuration
    if use_custom_user == "y" and user_login_field not in ["username", "email", "phone"]:
        print("ERROR: Invalid user login field. Must be 'username', 'email', or 'phone'")
        sys.exit(1)
    
    # Validate Celery configuration
    if use_celery == "y" and celery_broker not in ["redis", "rabbitmq"]:
        print("ERROR: Invalid Celery broker. Must be 'redis' or 'rabbitmq'")
        sys.exit(1)
    
    print(f"✓ Generating Django project: {project_name}")
    print(f"✓ Project slug: {project_slug}")
    if use_custom_user == "y":
        print(f"✓ Custom User model with login field: {user_login_field}")
    if use_celery == "y":
        print(f"✓ Celery configured with broker: {celery_broker}")

if __name__ == "__main__":
    main()
