# 🧠 LLM Streamlit App with Ollama

A clean and portable local chat app powered by [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/), letting you run open-source large language models like `mistral:7b` or `gemma3:1b` entirely offline. Use it locally or via Docker.

---

## 🚀 Features

* ✅ Modern Streamlit UI for chatting with LLMs
* ✅ Ollama service layer abstraction for flexibility
* ✅ Clean TOML configuration with Pydantic validation
* ✅ Docker support for containerized workflows
* ✅ Unit tests (`pytest`) for reliability

---

## 📦 Requirements

* **For local use**: Python 3.11+ and [Ollama installed](https://ollama.com/download)
* **For Docker**: [Docker](https://docs.docker.com/get-docker/) and **at least 7GB free disk space**
* At least one Ollama model pulled locally (e.g., `mistral:7b`, `gemma3:1b`, etc.)

To pull a model:

```bash
ollama pull gemma3:1b
```

---

## 🛠️ Setup & Usage

### 🔹 Option 1: Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/ahmedbellaaj10/llm-streamlit-app.git
cd llm-streamlit-app
```

**2. Configuration is already set up**

The app uses `config.toml` for configuration:

```toml
[ollama]
model_name = "gemma3:1b"
url = "http://localhost:11434"
```

You can edit this file to change the model or URL as needed.

**3. Start Ollama server**

```bash
ollama serve
```

**4. Install dependencies and launch the app**

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run src/app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

### 🔹 Option 2: Run with Docker

Make sure Docker is installed, then build and run the container:

```bash
# Build the Docker image
docker build -t llm-streamlit-app .

# Run the container
docker run -p 8501:8501 llm-streamlit-app
```

This will automatically:
- Start the Ollama server
- Pull the configured model
- Launch the Streamlit web UI at [http://localhost:8501](http://localhost:8501)

**Note**: First run requires ~7GB disk space and may take 3-5 minutes to download and set up everything.

---

### 🔹 Option 3: Run from Prebuilt Docker Image

The easiest way to get started! Simply pull and run the pre-built Docker image:

```bash
docker run -p 8501:8501 ahmedbellaaj10/llm-streamlit-app
```

That's it! The container will automatically:
- Start the Ollama server
- Pull the configured model (gemma3:1b)
- Launch the Streamlit web UI at [http://localhost:8501](http://localhost:8501)

No manual setup, no configuration needed - just one command, wait for environment to be ready (this might take some time) and you're ready to chat with your local LLM!

---

## 📁 Project Structure

```
llm-streamlit-app/
├── src/
│   ├── app.py
│   ├── config/
│   │   └── config.py
│   ├── services/
│   │   └── ollama_service.py
│   └── tests/
│       └── test_ollama_service.py
├── config.toml
├── requirements.txt
├── Dockerfile
├── entrypoint.sh
├── README.md
└── .gitignore
```


---

## ⚙️ Configuration

The app uses a clean TOML configuration file (`config.toml`) with Pydantic validation:

```toml
[ollama]
model_name = "gemma3:1b"  # The Ollama model to use
url = "http://localhost:11434"  # Ollama server URL
```

**Available models**: Any model available in Ollama (e.g., `mistral:7b`, `llama3.2:1b`, `qwen3:0.6b`)

---

## 🧪 Testing

Run all unit tests using:

```bash
pytest
```

---

## 🛠️ Roadmap

* [ ] Streamed/gradual responses
* [ ] Persistent chat history
* [ ] Model selector in UI
* [ ] Hosted Docker image & one-click cloud launch

---

## 📄 License

MIT License. Use freely, modify responsibly.

---

## 💬 Feedback & Contributions

Star ⭐ the repo or [open an issue](https://github.com/ahmedbellaaj10/llm-streamlit-app/issues) — contributions are always welcome!