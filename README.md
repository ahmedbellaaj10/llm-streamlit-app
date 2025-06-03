# 🧠 LLM Streamlit App with Ollama

A clean and portable local chat app powered by [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/), letting you run open-source large language models like `mistral:7b` or `gemma3:1b` entirely offline. Use it locally or via Docker.

---

## 🚀 Features

* ✅ Modern Streamlit UI for chatting with LLMs
* ✅ Ollama service layer abstraction for flexibility
* ✅ Easy `.env` configuration (no hardcoded values)
* ✅ Docker support for containerized workflows
* ✅ Unit tests (`pytest`) for reliability

---

## 📦 Requirements

* **For local use**: Python 3.8+ and [Ollama installed](https://ollama.com/download)
* **For Docker**: [Docker](https://docs.docker.com/get-docker/)
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

**2. Create your `.env` configuration**

```bash
cp .env.example .env
```

Edit `.env` to set your desired model and URL:

```
OLLAMA_MODEL_NAME="gemma3:1b"
OLLAMA_URL="http://localhost:11434"
```

**3. Make sure Ollama is running and your model is loaded**

```bash
ollama run gemma3:1b
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

This will launch the Streamlit web UI at [http://localhost:8501](http://localhost:8501)

---

### 🔹 Option 3: Run from Prebuilt Docker Image (Coming Soon!)

The project will soon be available as a pre-built Docker image on Docker Hub. Once published, you'll be able to run it with a single command. Stay tuned for updates!

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
├── .env.example
├── .env
├── requirements.txt
├── Dockerfile
├── entrypoint.sh
├── README.md
└── .gitignore
```

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

---

**Questions?**
If you run into issues or have ideas, [open a discussion](https://github.com/ahmedbellaaj10/llm-streamlit-app/discussions) or ping me on GitHub.
