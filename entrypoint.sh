#!/bin/sh

# Load environment variables from .env
export $(grep -v '^#' .env | xargs)

echo "🔧 Starting Ollama server..."
ollama serve &

# Wait until Ollama server is up
until curl -sf "${OLLAMA_URL}/api/tags" > /dev/null; do
  echo "Waiting for Ollama server to be ready at $OLLAMA_URL..."
  sleep 1
done

echo "🧠 Running the model: $OLLAMA_MODEL_NAME"
ollama run "$OLLAMA_MODEL_NAME" &

echo "🚀 Launching Streamlit app..."
streamlit run app.py
