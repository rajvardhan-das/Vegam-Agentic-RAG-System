from backend.ingest.cleaner import clean_text

raw = "Hello   world\n\n\nThis   is   text"
print(clean_text(raw))
