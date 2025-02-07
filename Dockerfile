# Pull official Python base image
FROM python:3.12.4-slim-bookworm

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y gcc curl && apt-get clean

# Install Poetry
RUN pip3 install poetry --no-cache-dir && poetry config virtualenvs.create false

# Copy dependency files
COPY pyproject.toml poetry.lock* /usr/src/app/

# Ensure poetry.lock exists to prevent build failure
RUN test -f /usr/src/app/poetry.lock || poetry lock

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root --no-cache

# Copy application code
COPY . .

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Ensure static files are collected
RUN poetry run python manage.py collectstatic --no-input

# Default command to start Gunicorn with multiple workers
#CMD ["gunicorn", "--chdir", "/usr/src/app", "--bind", "0.0.0.0:8001", "--workers", "3", "django_project.wsgi:application"]

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8001", "django_project.wsgi:application"]
