import requests

r = requests.post(
    "http://localhost:9000/mcp/query",
    json={"query": "What is apple?"}
)

print(r.json())
