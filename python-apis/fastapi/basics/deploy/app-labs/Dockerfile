FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN curl -Ls https://astral.sh/uv/install.sh | bash
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY . .

# Create virtual environment and install deps into system
RUN uv venv .venv && uv sync --system

# Start FastAPI using uv run
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4000"] 