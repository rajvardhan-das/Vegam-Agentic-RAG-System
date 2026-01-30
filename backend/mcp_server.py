from fastapi import FastAPI
from pydantic import BaseModel

from backend.ingest.pipeline import ingest_file
from backend.agents.orchestrator import handle_query

app = FastAPI(title="Agentic RAG MCP Server")


# ---------------------------
# Schemas
# ---------------------------

class QueryRequest(BaseModel):
    query: str


class IngestRequest(BaseModel):
    path: str


# ---------------------------
# MCP Tools
# ---------------------------

@app.post("/mcp/query")
def mcp_query(req: QueryRequest):
    """
    Tool: Answer a question using agentic RAG
    """
    result = handle_query(req.query)
    return {"result": result}


@app.post("/mcp/ingest")
def mcp_ingest(req: IngestRequest):
    """
    Tool: Ingest document into knowledge base
    """
    count = ingest_file(req.path)
    return {"chunks_added": count}
