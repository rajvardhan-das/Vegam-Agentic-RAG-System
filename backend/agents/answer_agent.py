from backend.services.llm import generate


def answer(query: str, context: str) -> str:
    """
    Generate final answer using LLM with retrieved context.
    """

    prompt = f"""
You are a helpful assistant.

Use ONLY the information in the context below to answer.
If the answer is not in the context, say you do not know.

Context:
{context}

Question:
{query}

Answer:
"""

    return generate(prompt)
