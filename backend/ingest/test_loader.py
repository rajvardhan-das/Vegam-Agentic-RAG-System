from backend.ingest.loader import load_document

text = load_document("data/uploads/generalized_news_intents_v1.xlsx")

print("Loaded text preview:\n")
print(text[:500])
