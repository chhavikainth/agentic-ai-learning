import time
from google import genai
from google.genai import errors
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

MODEL = "gemini-flash-lite-latest"

for attempt in range(5):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents="Explain what a neural network is in 2 sentences."
        )
        break
    except errors.ServerError:
        print(f"Attempt {attempt + 1}: server busy, waiting 10 seconds...")
        time.sleep(10)
else:
    raise SystemExit("Server still busy. Please try again in a few minutes.")

print(response.text)
print(response.candidates[0].finish_reason)
print(response.usage_metadata)