# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl and dependencies for uv
RUN apt-get update && apt-get install -y curl build-essential && \
    curl -Ls https://astral.sh/uv/install.sh | bash

# Ensure uv is available in PATH
ENV PATH="/root/.cargo/bin:$PATH"

# Copy dependency file
COPY pyproject.toml .

# Install Python packages using uv
RUN uv pip install --upgrade pip
RUN uv pip install fastapi uvicorn[standard]

# Copy the full app source code
COPY . .

# Expose the FastAPI port
EXPOSE 4000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:4000/health')"

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4000"] 