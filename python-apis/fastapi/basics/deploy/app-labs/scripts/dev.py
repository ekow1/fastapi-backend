#!/usr/bin/env python3
"""
Development helper script for App Labs API
"""
import subprocess
import sys
import os
from pathlib import Path


def run_command(command, description=""):
    """Run a command and handle errors"""
    if description:
        print(f"🔄 {description}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False


def main():
    """Main function to handle development tasks"""
    if len(sys.argv) < 2:
        print("""
🚀 App Labs API Development Helper

Usage: python scripts/dev.py <command>

Commands:
  install     - Install dependencies with uv
  run         - Run the application locally
  test        - Run tests
  lint        - Run linting (black, isort, flake8)
  format      - Format code with black and isort
  docker      - Build and run with Docker
  clean       - Clean up temporary files
  help        - Show this help message
        """)
        return

    command = sys.argv[1]
    
    if command == "install":
        print("📦 Installing dependencies...")
        run_command("uv sync", "Installing dependencies with uv")
        
    elif command == "run":
        print("🚀 Starting development server...")
        run_command("uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 4000", 
                   "Starting FastAPI server")
        
    elif command == "test":
        print("🧪 Running tests...")
        success = run_command("uv run pytest -v", "Running tests")
        if success:
            print("✅ All tests passed!")
        else:
            print("❌ Some tests failed!")
            sys.exit(1)
            
    elif command == "lint":
        print("🔍 Running linting...")
        success1 = run_command("uv run black --check .", "Checking code formatting")
        success2 = run_command("uv run isort --check-only .", "Checking import sorting")
        success3 = run_command("uv run flake8 .", "Running flake8")
        
        if success1 and success2 and success3:
            print("✅ All linting checks passed!")
        else:
            print("❌ Some linting checks failed!")
            sys.exit(1)
            
    elif command == "format":
        print("🎨 Formatting code...")
        run_command("uv run black .", "Formatting with black")
        run_command("uv run isort .", "Sorting imports with isort")
        print("✅ Code formatting complete!")
        
    elif command == "docker":
        print("🐳 Building and running with Docker...")
        run_command("docker build -t app-labs .", "Building Docker image")
        run_command("docker run -p 8000:8000 app-labs", "Running Docker container")
        
    elif command == "clean":
        print("🧹 Cleaning up...")
        # Remove Python cache files
        run_command("find . -type d -name __pycache__ -exec rm -rf {} +", "Removing __pycache__ directories")
        run_command("find . -name '*.pyc' -delete", "Removing .pyc files")
        run_command("find . -name '*.pyo' -delete", "Removing .pyo files")
        run_command("find . -name '*.pyd' -delete", "Removing .pyd files")
        
        # Remove test coverage files
        run_command("rm -rf .coverage htmlcov/", "Removing coverage files")
        
        # Remove build artifacts
        run_command("rm -rf build/ dist/ *.egg-info/", "Removing build artifacts")
        
        print("✅ Cleanup complete!")
        
    elif command == "help":
        main()  # Show help message
        
    else:
        print(f"❌ Unknown command: {command}")
        print("Run 'python scripts/dev.py help' for available commands")
        sys.exit(1)


if __name__ == "__main__":
    main() 