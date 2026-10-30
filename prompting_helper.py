import time
from google import genai
from google.genai import types, errors
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL = "gemini-flash-lite-latest"

def get_completion(prompt, system_prompt=""):
    config = types.GenerateContentConfig(
        system_instruction=system_prompt or None,
        temperature=0,
    )
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model=MODEL, contents=prompt, config=config
            )
            return response.text
        except errors.ServerError:
            print("Server busy, retrying in 10 seconds...")
            time.sleep(10)
    return "Server still busy, try again later."