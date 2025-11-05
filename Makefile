.PHONY: install install-dev test lint format clean build upload docs

# Default target
help:
	@echo "Smart Clipboard Manager - Development Commands"
	@echo ""
	@echo "install      Install the package in development mode"
	@echo "install-dev  Install with development dependencies"
	@echo "test         Run the test suite"
	@echo "lint         Run linting checks"
	@echo "format       Format code with black and isort"
	@echo "clean        Clean build artifacts"
	@echo "build        Build the package"
	@echo "upload       Upload to PyPI"
	@echo "docs         Generate documentation"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Testing
test:
	pytest tests/ --cov=src --cov-report=term-missing

test-verbose:
	pytest tests/ -v --cov=src --cov-report=html

# Code quality
lint:
	flake8 src/ tests/
	black --check src/ tests/
	isort --check-only src/ tests/

format:
	black src/ tests/
	isort src/ tests/

# Build and release
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*

upload-test: build
	python -m twine upload --repository testpypi dist/*

# Development
run:
	python main.py

run-gui:
	python main.py --show-ui

# System installation
install-system:
	./install-system.sh

# Documentation
docs:
	@echo "Documentation is in README.md and DEPLOYMENT.md"

# Quick development setup
setup: install-dev
	@echo "Development environment ready!"
	@echo "Run 'make test' to run tests"
	@echo "Run 'make run' to start the application"
