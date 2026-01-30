import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Agentic RAG Chatbot",
    layout="centered"
)

st.title("Agentic RAG Chatbot")

st.markdown("""
<style>

button {
    border-radius: 16px !important;
    background: linear-gradient(135deg, #b79cff, #d6c9ff) !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    box-shadow: 0 6px 18px rgba(140,120,255,0.35);
}

button:hover {
    transform: scale(1.02);
    opacity: 0.9;
}


</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Settings")

llm = st.sidebar.selectbox(
    "Choose LLM",
    ["ollama", "gemini"]
)

if st.sidebar.button("Apply LLM"):
    requests.post(
        f"{BACKEND_URL}/set-llm",
        json={"provider": llm}
    )
    st.sidebar.success(f"Using {llm}")

uploaded_file = st.sidebar.file_uploader("Upload Document")

if uploaded_file:
    files = {"file": uploaded_file}
    r = requests.post(
        f"{BACKEND_URL}/upload",
        files=files
    )
    st.sidebar.success(
        f"Uploaded {uploaded_file.name}"
    )

# -------------------------
# Chat
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    r = requests.post(
        f"{BACKEND_URL}/chat",
        json={"query": prompt}
    )

    data = r.json()

    if "answer" in data:
        answer = data["answer"]
    elif "detail" in data:
        answer = f"Error: {data['detail']}"
    else:
        answer = f"Unexpected response: {data}"


    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.chat_message("assistant").write(answer)
