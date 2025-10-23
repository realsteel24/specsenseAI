from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.getenv("GEMINI_KEY")
TEMPERATURE = 0.7
GEMINI_MODEL = "gemini-2.0-flash"
OLLAMA_MODEL = 'llama3:8b'
