# ───────────────────────────────────────────────────────────
# RoadGuard AI — Dockerfile for Render deployment
# ───────────────────────────────────────────────────────────
FROM python:3.11-slim

# System dependencies for OpenCV + ffmpeg for video re-encoding
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgl1-mesa-glx \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create runtime directories
RUN mkdir -p webapp/uploads webapp/outputs webapp/data

# Expose port (Render injects PORT env var)
EXPOSE 8000

# Launch
CMD ["python", "run.py"]
