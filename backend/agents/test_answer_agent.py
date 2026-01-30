from backend.agents.answer_agent import answer

context = "Paris is in France."
query = "Where is Paris?"

print(answer(query, context))
