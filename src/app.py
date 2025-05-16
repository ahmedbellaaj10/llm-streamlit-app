import requests
import streamlit as st

from config import get_env_variables
from ollama_runner import start_ollama_model

# Load environment variables
OLLAMA_MODEL, OLLAMA_URL = get_env_variables()

st.set_page_config(page_title="Local LLM with Ollama", page_icon=":robot_face:")
st.title(f"Chat with {OLLAMA_MODEL.capitalize()} via Ollama")

# Start the model (only once per session)
status = start_ollama_model(OLLAMA_MODEL, OLLAMA_URL)
st.info(status)

# Prompt UI
prompt = st.text_area("Enter your prompt", height=200)

if st.button("Send"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = requests.post(
                    f"{OLLAMA_URL}/api/generate",
                    json={
                        "prompt": prompt,
                        "model": OLLAMA_MODEL,
                        "stream": False,
                    },
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()
                st.text_area("Response", value=data.get("response", "No response returned."), height=200)
            except requests.RequestException as error:
                st.error(f"Error: {error}")