from backend.services.llm import generate


def plan(query: str) -> str:
    """
    Decide what action to take:
    - retrieve  -> needs document knowledge
    - direct    -> general reasoning / math / common knowledge
    """

    prompt = f"""
You are a planner agent.

Decide if the question needs information from a document knowledge base.

Examples:
Q: Where is Paris mentioned in the document?
A: retrieve

Q: Summarize the uploaded file.
A: retrieve

Q: What is 2 + 2?
A: direct

Q: Explain recursion.
A: direct

Now decide for this question.

Question:
{query}

Answer only one word: retrieve or direct.
"""

    decision = generate(prompt).strip().lower()

    if "retrieve" in decision:
        return "retrieve"
    else:
        return "direct"
