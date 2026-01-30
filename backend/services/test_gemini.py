import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

# Use a supported model ID
model = genai.GenerativeModel("gemini-2.5-flash")

resp = model.generate_content("Say hello in one sentence")
print(resp.text)
