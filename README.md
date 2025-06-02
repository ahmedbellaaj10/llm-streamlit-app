# 🧠 LLM Streamlit App with Ollama

This project is a clean local chat interface powered by [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/). It lets you run open-source LLMs like `mistral:7b` or `llama3` entirely offline through three flexible methods: local, Docker, or prebuilt image.

---

## 🚀 Features

- ✅ Streamlit UI for prompt-response chat
- ✅ Class-based service abstraction
- ✅ `.env` configuration
- ✅ Docker support
- ✅ Unit testing with `pytest`

---

## 📦 Requirements

- Python 3.8+ (for local usage)
- [Ollama installed](https://ollama.com/download) and accessible in terminal
- Docker + Docker Compose (for containerized usage)
- Ollama model pulled locally (e.g., `mistral:7b`)

```bash
ollama pull mistral:7b
```

---

## 🛠️ Setup Options

### 🔹 Option 1: Run Locally

#### 1. Clone the repository

```bash
git clone https://github.com/ahmedbellaaj10/llm-streamlit-app.git
cd llm-streamlit-app
```

#### 2. Create and configure `.env`

```bash
cp .env.example .env
```

Set values like:

```
OLLAMA_MODEL_NAME=mistral:7b
OLLAMA_URL=http://localhost:11434
```

#### 3.Make sure Ollama is running:
```bash
ollama run mistral:7b
```

#### 4. Install dependencies & run the app

```bash
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
streamlit run src/app.py
```

Make sure Ollama is running:
```bash
ollama run mistral:7b
```

---

### 🔹 Option 2: Run with Docker Compose

Ensure Docker and Docker Compose are installed.

```bash
docker-compose up --build
```

This will:
- Start the Ollama server
- Start the Streamlit app at [http://localhost:8501](http://localhost:8501)

---

### 🔹 Option 3: Run with Prebuilt Docker Image (Coming Soon)

When the official image is published to Docker Hub:

```bash
docker run -p 8501:8501 yourdockerhubusername/llm-streamlit-app
```

> ✅ Make sure Ollama is running separately or include it in your orchestration setup.

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
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## 🧪 Testing

```bash
pytest
```

---

## 🛠 Roadmap

- [ ] Streamed responses
- [ ] Chat history
- [ ] Model selector
- [ ] Hosted Docker image support

---

## 📄 License

MIT License. Use freely, modify responsibly.

---

## 💬 Feedback?

Star ⭐ the repo or open an issue — contributions welcome!
