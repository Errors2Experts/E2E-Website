# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Run Gunicorn server
CMD python manage.py migrate && gunicorn errors2experts.wsgi:application --bind 0.0.0.0:8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "errors2experts.wsgi:application"]