FROM python:3.11-slim as builder

# Install build dependencies and uv
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install uv

# Create and switch to a non-root user
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

# Copy only the files needed for installation
COPY --chown=appuser:appuser pyproject.toml .

# Create virtual environment and install dependencies
RUN uv venv /home/appuser/venv && \
    . /home/appuser/venv/bin/activate && \
    uv pip install \
    aiosqlite==0.20.0 \
    alembic==1.14.0 \
    boto3==1.35.92 \
    chromadb==0.6.1 \
    fastapi==0.115.6 \
    greenlet==3.1.1 \
    openai==1.59.3 \
    pydantic==2.10.4 \
    python-dotenv==1.0.1 \
    python-multipart==0.0.20 \
    tiktoken==0.8.0 \
    uvicorn==0.34.0 \
    ollama==0.3.3

# Final stage
FROM python:3.11-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to a non-root user
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

# Create data directories with proper permissions
RUN mkdir -p /home/appuser/data
RUN mkdir -p /home/appuser/chroma_db

# Copy virtual environment and application code
COPY --from=builder --chown=appuser:appuser /home/appuser/venv /home/appuser/venv
COPY --chown=appuser:appuser . .

# Make entrypoint script executable
RUN chmod +x /home/appuser/docker-entrypoint.sh

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV PATH="/home/appuser/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 8000

# Use the entrypoint script
ENTRYPOINT ["/home/appuser/docker-entrypoint.sh"] 