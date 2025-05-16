# 🧠 LLM Streamlit App with Ollama

This project is a minimal local chat interface powered by [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/), letting you run open-source LLMs like `mistral` entirely offline on your machine.

It provides a clean and extendable structure for local experimentation with LLMs through a simple web UI.

---

## 🚀 Features

- ✅ Auto-starts Ollama and loads your selected model
- ✅ Streamlit interface for prompt/response interaction
- ✅ Environment-based configuration using `.env`
- ✅ Clean project layout under `src/`

---

## 📦 Requirements

- Python 3.12+ (recommended, works on 3.8+)
- [Ollama](https://ollama.com/download) installed and accessible in your terminal
- `mistral` model pulled locally:
    ```bash
    ollama pull mistral
    ```

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/ahmedbellaaj10/llm-streamlit-app.git
cd llm-streamlit-app
```

---

### 2. Install `uv` (Fast Python Package Manager)

`uv` is a Rust-based package manager that replaces pip, venv, and pip-tools.

#### 🔧 Windows (PowerShell)
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

#### 💻 macOS/Linux
```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Test it:
```bash
uv --version
```

If not available, ensure the installation path (e.g., `~/.local/bin`) is in your system `PATH`.

---

### 3. Setup the Virtual Environment and Install Dependencies

```bash
uv venv
# Activate it
. .venv/Scripts/Activate.ps1   # Windows PowerShell

# or
source .venv/bin/activate        # macOS/Linux

# Install Python packages
uv pip install -r requirements.txt
```

---

### 4. Create the `.env` File

A sample file `.env.example` is provided. You can copy it:

```bash
cp .env.example .env
```

Then adjust it if needed.

---

### 5. Run the App

```bash
streamlit run src/app.py
```

Then go to [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
llm-streamlit-app/
├── .env.example
├── .env                  # (Not tracked)
├── requirements.txt
├── README.md
├── src/
│   ├── app.py
│   ├── config.py
│   └── ollama_runner.py
├── .gitignore
└── LICENSE
```

---

## 📄 License

MIT License. Use freely, modify responsibly.


---

## 🛠 Next Ideas (Coming Soon)

- [ ] Streamed responses
- [ ] Dockerization
- [ ] Model switching
- [ ] Chat history

---

## 💬 Feedback?

Feel free to open issues or contribute improvements. Star ⭐ the repo if this helped!
