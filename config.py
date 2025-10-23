from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("GEMINI_KEY")
gemini_model = "gemini-2.0-flash"
ollama_model = 'llama2:latest'    