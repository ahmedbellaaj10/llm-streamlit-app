FROM python:3.11-slim

WORKDIR /app

# Install required system packages
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy application code and configuration
COPY src/ ./src/
COPY config.toml .
COPY entrypoint.sh .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

# Expose ports
EXPOSE 8501 11434

# Run the application
CMD ["./entrypoint.sh"]
