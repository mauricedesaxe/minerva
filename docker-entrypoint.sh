#!/bin/sh
set -e

# Run database migrations
alembic upgrade head

# Start the application
exec uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000} 