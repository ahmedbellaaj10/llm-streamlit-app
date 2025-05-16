import subprocess
import time
import requests
import atexit

OLLAMA_PROCESS = None


def start_ollama_model(model, base_url):
    """Start the Ollama model subprocess if not already running."""
    global OLLAMA_PROCESS

    try:
        response = requests.get(f"{base_url}/api/tags", timeout=2)
        if response.status_code == 200:
            return "Ollama is already running."
    except requests.RequestException:
        pass

    OLLAMA_PROCESS = subprocess.Popen(["ollama", "run", model])

    for _ in range(10):
        try:
            response = requests.get(f"{base_url}/api/tags", timeout=2)
            if response.status_code == 200:
                return "Ollama started successfully."
        except requests.RequestException:
            time.sleep(1)

    return "Failed to start Ollama."


def stop_ollama():
    """Ensure the Ollama subprocess is stopped on app exit."""
    global OLLAMA_PROCESS
    if OLLAMA_PROCESS is not None:
        OLLAMA_PROCESS.terminate()

atexit.register(stop_ollama)