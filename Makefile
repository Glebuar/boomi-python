# Boomi API SDK - Development Makefile

.PHONY: help install install-dev run-examples lint format clean docs

# Default target
help:
	@echo "Boomi API SDK Development Commands"
	@echo "================================="
	@echo ""
	@echo "Setup:"
	@echo "  install        Install production dependencies"
	@echo "  install-dev    Install development dependencies"
	@echo ""
	@echo "Examples:"
	@echo "  run-examples   Run example scripts (requires BOOMI_* env vars)"
	@echo ""
	@echo "Code Quality:"
	@echo "  lint           Run linting checks"
	@echo "  format         Format code"
	@echo ""
	@echo "Maintenance:"
	@echo "  clean          Clean temporary files"
	@echo "  docs           Generate documentation"

# Installation targets
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Examples (validation via real API)
run-examples:
	@echo "Running example scripts..."
	@echo "NOTE: Set BOOMI_ACCOUNT, BOOMI_USER, BOOMI_SECRET environment variables"
	@for file in examples/12_utilities/*.py; do \
		echo "Running $$file..."; \
		PYTHONPATH=src python3 "$$file" || true; \
	done

# Code quality targets
lint:
	@echo "Running basic Python syntax checks..."
	python -m py_compile src/boomi/__init__.py
	python -m py_compile src/boomi/sdk.py
	@echo "✅ Basic lint checks passed"

format:
	@echo "Code formatting would go here (black, isort, etc.)"
	@echo "Run: pip install black isort && black . && isort ."

# Maintenance targets
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

docs:
	@echo "Documentation generation would go here"
	@echo "Consider using Sphinx or similar tools"

# Utility targets
check-deps:
	@echo "Checking if required dependencies are installed..."
	python -c "import requests; print('✅ requests')"
	python -c "import dotenv; print('✅ python-dotenv')"
	python -c "import boomi; print('✅ boomi SDK')"

setup-env:
	@echo "Setting up development environment..."
	@echo "1. Copy .env.example to .env (if it exists)"
	@echo "2. Update .env with your Boomi credentials"
	@echo "3. Run 'make install-dev' to install dependencies"
	@echo "4. Run 'make run-examples' to validate setup"