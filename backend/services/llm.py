import requests
import google.generativeai as genai
from backend.utils.exceptions import LLMError
from backend.utils.logger import logger


from backend.config import GEMINI_API_KEY, get_llm_provider


# -------------------------
# Gemini Provider
# -------------------------

def gemini_generate(prompt: str) -> str:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


# -------------------------
# Ollama Provider
# -------------------------

def ollama_generate(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3:8b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"]


# -------------------------
# Unified Interface
# -------------------------

def generate(prompt: str) -> str:
    provider = get_llm_provider()

    if provider == "ollama":
        return ollama_generate(prompt)
    elif provider == "gemini":
        return gemini_generate(prompt)
    else:
        raise ValueError("Unsupported LLM provider")
