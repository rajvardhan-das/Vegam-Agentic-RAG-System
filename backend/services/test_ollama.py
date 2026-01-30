import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3:8b",
    "prompt": "Explain what a vector database is in one sentence.",
    "stream": False
}

response = requests.post(url, json=payload)
print(response.json()["response"])
