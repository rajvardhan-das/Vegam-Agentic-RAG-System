import json
from pathlib import Path

# Path to config.json
CONFIG_PATH = Path(__file__).parent / "config.json"

# Load config file
with open(CONFIG_PATH, "r") as f:
    _config = json.load(f)

# Static values
GEMINI_API_KEY = _config.get("GEMINI_API_KEY")
DEFAULT_LLM_PROVIDER = _config.get("DEFAULT_LLM_PROVIDER", "ollama")

# Runtime state (can change while app is running)
_CURRENT_LLM_PROVIDER = DEFAULT_LLM_PROVIDER


def get_llm_provider() -> str:
    """
    Returns currently active LLM provider.
    """
    return _CURRENT_LLM_PROVIDER


def set_llm_provider(provider: str):
    """
    Change active LLM provider at runtime.
    """
    global _CURRENT_LLM_PROVIDER

    if provider not in ["ollama", "gemini"]:
        raise ValueError("Provider must be either 'ollama' or 'gemini'")

    _CURRENT_LLM_PROVIDER = provider
