import time
from google import genai
from google.genai import types, errors
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL = "gemini-flash-lite-latest"

SYSTEM_PROMPT = "You are a friendly tutor who explains data science concepts simply."

history = []   # the conversation so far: this is the chatbot's "memory"

def ask_model(history):
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    for attempt in range(5):
        try:
            return client.models.generate_content(
                model=MODEL, contents=history, config=config
            )
        except errors.ServerError:
            print("(Server busy, retrying in 10 seconds...)")
            time.sleep(10)
    return None

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    # 1. Add your message to the history
    history.append({"role": "user", "parts": [{"text": user_input}]})

    # 2. Send the WHOLE history to the model
    response = ask_model(history)
    if response is None:
        print("Bot: Sorry, the server is busy. Please try again.")
        history.pop()   # remove the message that didn't get an answer
        continue

    # 3. Add the model's reply to the history
    reply = response.text
    history.append({"role": "model", "parts": [{"text": reply}]})

    # 4. Show the reply and the tokens used
    print(f"\nBot: {reply}")
    print(f"(tokens this turn: {response.usage_metadata.total_token_count})\n")