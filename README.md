# Agentic AI Learning

My notes and code while learning to build AI agents, from first API calls to tool use, RAG and evaluation. All code is written by me and runs on the free Gemini API.

## Progress
- [x] First API call with the Gemini API
- [x] Chatbot with conversation memory
- [ ] Prompt engineering exercises (chapters 1–3 done)
- [ ] First tool-using agent
- [ ] RAG over documents
- [ ] Agent evaluation

## Files
| File | What it does |
|---|---|
| `first_call.py` | Sends a question to Gemini and prints the answer, finish reason and token usage. Retries automatically if the server is busy. |
| `prompting_helper.py` | A reusable `get_completion()` function with system prompt support and retry logic. |
| `prompting_ch3.py` | Compares answers with and without a role (system prompt). |
| `chatbot.py` | A command-line chatbot that remembers the conversation by resending the full message history each turn. |

## What I've learned so far
- LLMs have no memory between calls. A chatbot "remembers" only because the code resends the whole conversation each time.
- Token usage grows with every turn for the same reason, which is why managing context matters for agents.
- A system prompt (role) changes the tone, structure and depth of answers.
- Real APIs can be busy or retire models, so production code needs retry logic.

## Tools
Python, Gemini API (`google-genai`), python-dotenv
