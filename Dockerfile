FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first so this layer is cached when code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY main.py ./
COPY app/ ./app/
COPY routers/ ./routers/
COPY services/ ./services/

EXPOSE 8000

# Run the ASGI app on all interfaces so the container is reachable
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
