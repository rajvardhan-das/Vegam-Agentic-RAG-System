from backend.agents.planner import plan
from backend.agents.retriever import retrieve
from backend.agents.context_builder import build_context
from backend.agents.answer_agent import answer
from backend.services.llm import generate


def handle_query(query: str) -> str:
    """
    Main agentic orchestration function.
    """

    decision = plan(query)

    if decision == "direct":
        # No retrieval needed
        return generate(query)

    # Retrieval path
    chunks = retrieve(query)
    context = build_context(chunks)
    return answer(query, context)
