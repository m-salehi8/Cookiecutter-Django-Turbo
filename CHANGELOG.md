# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Docker support with Dockerfile and docker-compose.yml
- Environment configuration files (.env.example, .env.docker.example)
- Modular Django settings structure (base.py, local.py, production.py)
- ASGI configuration for async support
- Pre-commit configuration for code quality
- Comprehensive documentation and contributing guidelines
- MIT License

### Changed
- Refactored Django settings into modular structure
- Updated project structure for better organization
- Enhanced cookiecutter.json configuration options
- Improved post-generation hook with detailed setup instructions

### Fixed
- Typo in post-generation hook filename reference
- Updated requirements.txt with proper dependencies
- Fixed URL configuration structure

## [1.0.0] - 2024-01-XX

### Added
- Initial release of CookieCutter Django Turbo
- Support for multiple database backends (PostgreSQL, MySQL, SQLite)
- Custom User model with flexible authentication options
- Django REST Framework integration
- Redis caching support
- Celery task queue integration
- Beautiful home page template
- Comprehensive configuration options
- Production-ready settings
- Testing setup with pytest
- Code quality tools (Black, flake8, isort)

### Features
- **Database Options**: PostgreSQL, MySQL, SQLite
- **Authentication**: Username, Email, Phone login options
- **API Framework**: Django REST Framework with optional JWT
- **Caching**: Redis support
- **Task Queue**: Celery with Redis/RabbitMQ brokers
- **Documentation**: Optional API documentation with Swagger/ReDoc
- **Code Quality**: Pre-commit hooks and linting tools
- **Production Ready**: Gunicorn, WhiteNoise, comprehensive logging

---

## Version History

- **v1.0.0**: Initial release with core Django features
- **Unreleased**: Docker support, modular settings, enhanced documentation

## Migration Guide

### From v1.0.0 to Unreleased

If you have an existing project generated with v1.0.0, consider these updates:

1. **Settings Structure**: The settings.py has been split into modular files:
   - `core/settings/base.py` - Base settings
   - `core/settings/local.py` - Development settings
   - `core/settings/production.py` - Production settings

2. **Docker Support**: New Docker files have been added:
   - `Dockerfile` - Container configuration
   - `docker-compose.yml` - Multi-service setup
   - `.env.docker.example` - Docker-specific environment variables

3. **Environment Configuration**: Enhanced environment variable management:
   - `.env.example` - Local development configuration
   - `.env.docker.example` - Docker development configuration

4. **Code Quality**: Pre-commit hooks have been added:
   - `.pre-commit-config.yaml` - Pre-commit configuration
   - Enhanced code formatting and linting

## Support

For questions about version compatibility or migration, please open an issue on GitHub.
