#!/bin/sh
set -e

echo "🔧 Loading configuration..."
MODEL_NAME=$(python3 -c "from src.config.config import get_config; print(get_config().model_name)")
OLLAMA_URL=$(python3 -c "from src.config.config import get_config; print(get_config().url)")

echo "🚀 Starting Ollama server..."
ollama serve &

echo "⏳ Waiting for Ollama server to be ready..."
until curl -sf "$OLLAMA_URL/api/tags" > /dev/null 2>&1; do
  sleep 1
done

echo "📦 Pulling model: $MODEL_NAME"
ollama pull "$MODEL_NAME"

echo "🌐 Starting Streamlit application..."
cd src && streamlit run app.py