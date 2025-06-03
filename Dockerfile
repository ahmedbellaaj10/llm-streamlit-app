FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl gnupg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY ./src .
COPY .env .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

# Add these lines:
ARG OLLAMA_MODEL_NAME
ENV OLLAMA_MODEL_NAME=$OLLAMA_MODEL_NAME

RUN ollama serve & sleep 3 && ollama pull "$OLLAMA_MODEL_NAME" && pkill ollama

EXPOSE 8501
EXPOSE 11434

SHELL ["/bin/sh", "-c"]

CMD ["./entrypoint.sh"]
