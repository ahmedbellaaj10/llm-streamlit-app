import streamlit as st
from config.config import get_env_variables
from services.ollama_service import OllamaClient

# Load environment variables
OLLAMA_MODEL, OLLAMA_URL = get_env_variables()
ollama = OllamaClient(model=OLLAMA_MODEL, base_url=OLLAMA_URL)

st.set_page_config(page_title="Chat with Ollama LLM", page_icon="👨‍💼")
st.title(f"Chat with {OLLAMA_MODEL.capitalize()} via Ollama")

# Basic health checks (fast)
if not ollama.check_health():
    st.error("Ollama server is not running. Run it or ensure you have Ollama installed.")
elif not ollama.model_exists():
    st.error(f"Model '{OLLAMA_MODEL}' is not available. Ensure it's pulled.")
else:
    with st.container():
        with st.expander("✅ Environment Check Passed", expanded=True):
            st.success("Ollama server and model are available.")
            st.info(f"Reminder: Make sure you've run the model using: `ollama run {OLLAMA_MODEL}`")
            st.warning("⚠️ First response may be slower if the model is cold-starting.")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User prompt input
    prompt = st.chat_input("Enter your message")
    if prompt:
        # Store user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Show loading and get response
        with st.spinner("Generating response..."):
            response = ollama.query_model(prompt)

        # Store assistant response
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Display chat history (after input so newest is at the end)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Auto-scroll to latest
    st.markdown("<div id='end'></div>", unsafe_allow_html=True)
    st.markdown("<script>document.getElementById('end').scrollIntoView();</script>", unsafe_allow_html=True)
