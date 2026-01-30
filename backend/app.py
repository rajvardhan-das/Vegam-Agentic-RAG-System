from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
from pathlib import Path

from backend.ingest.pipeline import ingest_file
from backend.agents.orchestrator import handle_query
from backend.config import set_llm_provider

app = FastAPI(title="Agentic RAG Backend")

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------
# Schemas
# -------------------------

class QueryRequest(BaseModel):
    query: str


class LLMRequest(BaseModel):
    provider: str


# -------------------------
# Health
# -------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------
# Upload & Ingest
# -------------------------

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_path = UPLOAD_DIR / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        chunks = ingest_file(str(file_path))

        return {
            "filename": file.filename,
            "chunks_added": chunks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# Chat
# -------------------------

@app.post("/chat")
def chat(req: QueryRequest):
    try:
        answer = handle_query(req.query)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# Switch LLM
# -------------------------

@app.post("/set-llm")
def set_llm(req: LLMRequest):
    set_llm_provider(req.provider)
    return {"active_llm": req.provider}
