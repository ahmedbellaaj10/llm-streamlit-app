import tomllib
from pathlib import Path
from pydantic import BaseModel, HttpUrl, ConfigDict

class OllamaConfig(BaseModel):
    model_config = ConfigDict(protected_namespaces=())
    
    model_name: str
    url: HttpUrl

def get_config() -> OllamaConfig:
    """Load configuration from config.toml
    
    Looks for config.toml in:
    1. Current working directory (for local development)
    2. Project root (when running from src/)
    """
    config_paths = [
        Path("config.toml"),                    # Current directory
        Path("../config.toml"),                 # Parent directory (from src/)
        Path(__file__).parent.parent.parent / "config.toml"  # Project root
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            with open(config_path, "rb") as f:
                data = tomllib.load(f)
            return OllamaConfig(**data["ollama"])
    
    raise FileNotFoundError("config.toml not found. Please ensure it exists in the project root.")

# Backward compatibility
def get_env_variables():
    """Legacy function for compatibility"""
    config = get_config()
    return config.model_name, str(config.url)