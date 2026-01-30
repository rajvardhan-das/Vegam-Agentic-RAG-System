from backend.ingest.pipeline import ingest_file

count = ingest_file("data\Rajvardhan Das Resume.pdf")
print("Chunks stored:", count)
