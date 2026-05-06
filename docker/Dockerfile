# docker/Dockerfile
# Base image: slim Python 3.11 — small size, production appropriate
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
# libgomp1: required by Prophet and LightGBM for parallel processing
# gcc: required to compile some Python packages
RUN apt-get update && apt-get install -y \
    libgomp1 \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first — Docker caches this layer
# If requirements.txt hasn't changed, Docker skips reinstalling
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY app/ ./app/
COPY params.yaml .
COPY data/processed/ ./data/processed/
COPY data/features/ ./data/features/
COPY reports/ ./reports/
COPY models/ ./models/

# Expose Streamlit port
EXPOSE 8501

# Health check — Streamlit responds on /healthz
HEALTHCHECK CMD curl --fail http://localhost:8501/healthz || exit 1

# Run Streamlit app
CMD ["streamlit", "run", "app/streamlit_app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--browser.gatherUsageStats=false"]
