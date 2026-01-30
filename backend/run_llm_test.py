from backend.config import set_llm_provider
from backend.services.llm import generate

print("Choose LLM provider:")
print("1 - ollama (local)")
print("2 - gemini (cloud)")

choice = input("Enter choice (1 or 2): ").strip()

if choice == "1":
    set_llm_provider("ollama")
elif choice == "2":
    set_llm_provider("gemini")
else:
    print("Invalid choice, defaulting to ollama")
    set_llm_provider("ollama")

prompt = input("Enter your prompt: ")

response = generate(prompt)
print("\n--- LLM RESPONSE ---")
print(response)
