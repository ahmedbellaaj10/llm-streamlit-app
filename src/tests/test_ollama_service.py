from unittest.mock import patch
from services.ollama_service import OllamaClient

@patch("services.ollama_service.requests.get")
def test_check_health(mock_get):
    mock_get.return_value.status_code = 200
    client = OllamaClient("llama3", "http://localhost:11434")
    assert client.check_health() is True

@patch("services.ollama_service.requests.get")
def test_model_exists_true(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"models": [{"name": "llama3"}]}
    client = OllamaClient("llama3", "http://localhost:11434")
    assert client.model_exists() is True

@patch("services.ollama_service.requests.post")
def test_query_model_success(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"response": "Hello there!"}
    client = OllamaClient("llama3", "http://localhost:11434")
    result = client.query_model("Hi")
    assert result == "Hello there!"