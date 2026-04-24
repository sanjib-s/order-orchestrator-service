FROM python:3.11-alpine

# Create non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

WORKDIR /app

# Install dependencies as root, then switch to non-root user
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --retries 3 --timeout 60 -r requirements.txt

# Change ownership and switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser

COPY main.py .

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]