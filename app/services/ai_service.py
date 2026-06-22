import os
from http.client import responses

import google.generativeai as genai
from click import prompt

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key = os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def summarize_text(text: str):

    prompt = f"""
    Summarize this following support conversation
    in 2-3 concise sentences:
    
    {text}
"""

    response = model.generate_content(prompt)

    return response.text