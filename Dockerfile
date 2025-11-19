## Parent image
FROM python:3.13.3-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

## Work directory inside the docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copy requirements first for better caching
COPY requirements.txt pyproject.toml setup.py ./

## Install dependencies
RUN pip install --no-cache-dir -e .

## Copy application code
COPY . .

## Create necessary directories
RUN mkdir -p logs data chroma_db

## Build the pipeline (create processed data and vector store)
RUN python pipeline/build_pipeline.py

# Used PORTS
EXPOSE 8501

# Run the app 
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]