# --- Stage 1: Builder ---
FROM python:3.12-slim AS builder 
# Note: Python 3.14 is currently in "Alpha/Pre-release". 
# 3.12 or 3.13 is recommended for stability.

WORKDIR /app
COPY requirements.txt .

# Create a Virtual Environment
RUN python -m venv /opt/venv
# Use the venv to install requirements
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# --- Stage 2: Final ---
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    dumb-init \
    && rm -rf /var/lib/apt/lists/*

# Copy the ENTIRE virtual environment
COPY --from=builder /opt/venv /opt/venv
COPY main.py models.py faker_util.py ./

# Ensure PATH uses the Virtual Environment
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN useradd -m -u 1001 appuser && \
    chown -R appuser:appuser /app /opt/venv

USER appuser

EXPOSE 8000

ENTRYPOINT ["dumb-init", "--"]
# Now 'uvicorn' will be found perfectly in /opt/venv/bin
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]