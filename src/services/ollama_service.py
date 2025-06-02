import requests
import logging

class OllamaClient:
    def __init__(self, model: str, base_url: str):
        self.model = model
        self.base_url = base_url.rstrip("/")
        logging.basicConfig(level=logging.INFO)

    def check_health(self) -> bool:
        """Check if the Ollama server is responding."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def model_exists(self) -> bool:
        """Check if the specified model is available."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            models = response.json().get("models", [])
            return any(m.get("name", "").startswith(self.model) for m in models)
        except requests.RequestException:
            return False

    def query_model(self, prompt: str) -> str:
        """Send a prompt to the model and get a response."""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"prompt": prompt, "model": self.model, "stream": False},
                timeout=30
            )
            response.raise_for_status()
            return response.json().get("response", "No response returned.")
        except requests.RequestException as e:
            logging.error(f"Ollama query failed: {e}")
            return f"Error: {e}"