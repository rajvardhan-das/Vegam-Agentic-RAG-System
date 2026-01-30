from backend.ingest.loader import load_document

text = load_document("data\Rajvardhan Das Resume.pdf")

print("Loaded text preview:\n")
print(text[:500])
