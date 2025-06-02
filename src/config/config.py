import os
from dotenv import load_dotenv

def get_env_variables():
    load_dotenv()
    model = os.getenv("OLLAMA_MODEL_NAME")
    url = os.getenv("OLLAMA_URL")
    if not model or not url:
        raise EnvironmentError("OLLAMA_MODEL_NAME or OLLAMA_URL not set in .env")
    return model, url