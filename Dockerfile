FROM python:3.10-slim

# Create user with UID 1000 (Hugging Face default)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Install lightweight dependencies (FastEmbed ONNX - ultra low memory)
COPY --chown=user ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Pre-cache nomic embedding model inside Docker image for instant queries
RUN python -c "from fastembed import TextEmbedding; TextEmbedding(model_name='nomic-ai/nomic-embed-text-v1.5')" || true

# Copy application files
COPY --chown=user . /app

# Expose port 7860 (Hugging Face default)
EXPOSE 7860

# Start FastAPI application with dynamic port fallback
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-7860}"]
