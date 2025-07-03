.PHONY: help install run test lint format docker clean build

# Default target
help:
	@echo "🚀 App Labs API - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install dependencies with uv"
	@echo "  make run        - Run the application locally"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code with black and isort"
	@echo "  make docker     - Build and run with Docker"
	@echo "  make clean      - Clean up temporary files"
	@echo "  make build      - Build Docker image"
	@echo "  make deploy     - Deploy to production (placeholder)"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	uv sync

# Run the application
run:
	@echo "🚀 Starting development server..."
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 4000

# Run tests
test:
	@echo "🧪 Running tests..."
	uv run pytest -v

# Run tests with coverage
test-cov:
	@echo "🧪 Running tests with coverage..."
	uv run pytest --cov=app --cov-report=html --cov-report=term

# Run linting
lint:
	@echo "🔍 Running linting checks..."
	uv run black --check .
	uv run isort --check-only .
	uv run flake8 .

# Format code
format:
	@echo "🎨 Formatting code..."
	uv run black .
	uv run isort .

# Build Docker image
build:
	@echo "🐳 Building Docker image..."
	docker build -t app-labs .

# Run with Docker
docker: build
	@echo "🐳 Running with Docker..."
	docker run -p 4000:4000 app-labs

# Run with Docker Compose
docker-compose:
	@echo "🐳 Running with Docker Compose..."
	docker-compose -f docker-stack.yml up --build

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name '*.pyc' -delete 2>/dev/null || true
	find . -name '*.pyo' -delete 2>/dev/null || true
	find . -name '*.pyd' -delete 2>/dev/null || true
	rm -rf .coverage htmlcov/ 2>/dev/null || true
	rm -rf build/ dist/ *.egg-info/ 2>/dev/null || true
	rm -rf .pytest_cache/ 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Deploy (placeholder)
deploy:
	@echo "🚀 Deploying to production..."
	@echo "This is a placeholder. Configure your deployment in .github/workflows/deploy.yml"
	@echo "Available deployment options:"
	@echo "  - Docker Hub"
	@echo "  - Railway"
	@echo "  - Heroku"
	@echo "  - AWS ECS"

# Development setup
setup: install
	@echo "✅ Development environment setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Run 'make run' to start the development server"
	@echo "  2. Visit http://localhost:8000/docs for API documentation"
	@echo "  3. Run 'make test' to run tests"
	@echo "  4. Run 'make lint' to check code quality"

# Full development workflow
dev: format lint test
	@echo "✅ Development workflow complete!"

# Production build
prod: clean build
	@echo "✅ Production build complete!" 