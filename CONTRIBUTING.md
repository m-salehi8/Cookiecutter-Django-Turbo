# Contributing to CookieCutter Django Turbo

Thank you for your interest in contributing to CookieCutter Django Turbo! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use Black for code formatting
- Use isort for import sorting
- Use flake8 for linting
- Maximum line length: 88 characters

### Pre-commit Hooks
The project uses pre-commit hooks to ensure code quality:
```bash
pre-commit install
pre-commit run --all-files
```

### Testing
- Write tests for new features
- Ensure all tests pass before submitting
- Use pytest for testing

## 🏗️ Project Structure

```
cookiecutter-django-turbo/
├── {{cookiecutter.project_slug}}/          # Generated project template
│   ├── core/                              # Django settings & config
│   ├── user/                              # Custom user app
│   ├── Dockerfile                         # Docker configuration
│   ├── docker-compose.yml                 # Docker Compose setup
│   └── requirements.txt                   # Python dependencies
├── hooks/                                 # Pre/post generation hooks
├── cookiecutter.json                      # Template configuration
└── README.md                              # Project documentation
```

## 🔧 Adding New Features

### New Configuration Options
1. Add the option to `cookiecutter.json`
2. Update the README.md with the new option
3. Modify relevant template files
4. Update post-generation hook if needed
5. Add tests for the new feature

### New Dependencies
1. Add to `requirements.txt` with conditional inclusion
2. Update documentation
3. Test with different configurations

## 🐛 Bug Reports

When reporting bugs, please include:
- CookieCutter version
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

## 💡 Feature Requests

Feature requests are welcome! Please provide:
- Clear description of the feature
- Use case and motivation
- Potential implementation approach (if you have ideas)

## 📝 Pull Request Process

1. Ensure your branch is up to date with the main branch
2. Run all tests and pre-commit hooks
3. Update documentation if needed
4. Provide a clear description of changes
5. Reference any related issues

## 🏷️ Release Process

Releases are managed by maintainers and follow semantic versioning:
- `MAJOR`: Breaking changes
- `MINOR`: New features (backward compatible)
- `PATCH`: Bug fixes (backward compatible)

## 📞 Getting Help

- Open an issue for bugs or feature requests
- Check existing issues and discussions
- Review the README.md for documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CookieCutter Django Turbo! 🎉
