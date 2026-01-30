from backend.agents.context_builder import build_context

chunks = [
    "Paris is the capital of France.",
    "France is in Europe.",
    "Paris has the Eiffel Tower."
]

context = build_context(chunks)

print(context)
