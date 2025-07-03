# App Labs API

A FastAPI application with GitHub Actions deployment using uv and uvicorn.

## Features

- 🚀 FastAPI with automatic API documentation
- 📦 uv for fast dependency management
- 🐳 Docker containerization
- 🔄 GitHub Actions CI/CD pipeline
- 🧪 Comprehensive testing setup
- 🔒 Security scanning with Trivy
- 📊 Code coverage reporting

## Quick Start

### Prerequisites

- Python 3.9+
- uv (Python package manager)
- Docker (optional)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd app-labs
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the application**
   ```bash
   uv run uvicorn app.main:app --reload
   ```

4. **Access the API**
   - API: http://localhost:4000
   - Documentation: http://localhost:4000/docs
   - ReDoc: http://localhost:4000/redoc

### Using Docker

1. **Build and run with Docker Compose**
   ```bash
   docker-compose -f docker-stack.yml up --build
   ```

2. **Or build and run manually**
   ```bash
   docker build -t app-labs .
   docker run -p 8000:8000 app-labs
   ```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/items` | Get all items |
| GET | `/items/{id}` | Get specific item |
| POST | `/items` | Create new item |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

### Example Usage

```bash
# Get all items
curl http://localhost:4000/items

# Create a new item
curl -X POST http://localhost:4000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Item", "price": 29.99, "description": "A sample item"}'

# Get a specific item
curl http://localhost:4000/items/1

# Update an item
curl -X PUT http://localhost:4000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "price": 39.99}'

# Delete an item
curl -X DELETE http://localhost:4000/items/1
```

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app --cov-report=html

# Run specific test file
uv run pytest tests/test_main.py
```

### Code Quality

```bash
# Format code
uv run black .

# Sort imports
uv run isort .

# Lint code
uv run flake8 .
```

### Pre-commit Hooks

Install pre-commit hooks for automatic code formatting:

```bash
uv run pre-commit install
```

## Deployment

### GitHub Actions

The project includes a comprehensive GitHub Actions workflow that:

1. **Tests** the application on multiple Python versions
2. **Lints** code with black, isort, and flake8
3. **Builds** Docker image
4. **Scans** for security vulnerabilities
5. **Deploys** to your chosen platform

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Application port | 8000 |
| `HOST` | Application host | 0.0.0.0 |
| `ENVIRONMENT` | Environment mode | production |

### Deployment Options

The GitHub Actions workflow includes deployment options for:

- **EC2**: Direct deployment to EC2 instance (enabled by default)
- **Railway**: Deploy to Railway platform
- **Heroku**: Deploy to Heroku

#### EC2 Deployment with Docker Stack (Recommended)

The workflow is configured to deploy directly to your EC2 instance using Docker Stack. To set this up:

1. **Add GitHub Secrets**:
   - `EC2_HOST`: Your EC2 instance public IP or domain
   - `EC2_USER`: SSH username (usually `ubuntu`)
   - `EC2_KEY`: Your private SSH key for EC2 access

2. **Prepare your EC2 instance**:
   ```bash
   # Install Docker
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo usermod -aG docker $USER
   sudo systemctl enable docker
   sudo systemctl start docker
   
   # Initialize Docker Swarm
   sudo docker swarm init
   
   # Install Git
   sudo apt-get install -y git
   ```

3. **Configure EC2 Security Group**:
   - Allow inbound traffic on port 22 (SSH)
   - Allow inbound traffic on port 4000 (API)
   - Or use a load balancer/nginx for port 80/443

4. **Manual Docker Stack management** (if needed):
   ```bash
   # On your EC2 instance
   chmod +x scripts/swarm-manage.sh
   
   # Deploy stack
   ./scripts/swarm-manage.sh deploy
   
   # Check status
   ./scripts/swarm-manage.sh status
   
   # View logs
   ./scripts/swarm-manage.sh logs
   
   # Health check
   ./scripts/swarm-manage.sh health
   ```

To enable other deployment options:

1. Add the required secrets to your GitHub repository
2. Uncomment the relevant deployment section in `.github/workflows/deploy.yml`

### Manual Deployment

```bash
# Build Docker image
docker build -t app-labs .

# Push to registry
docker tag app-labs your-registry/app-labs:latest
docker push your-registry/app-labs:latest

# Deploy to your platform
# (Follow your platform's specific deployment instructions)
```

## Project Structure

```
app-labs/
├── app/
│   └── main.py              # FastAPI application
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── Dockerfile               # Docker configuration
├── docker-stack.yml         # Docker Compose for development
├── pyproject.toml          # Project configuration and dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/app-labs/issues) page
2. Create a new issue with detailed information
3. Include logs and error messages when applicable

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [GitHub Actions](https://github.com/features/actions) - CI/CD platform 