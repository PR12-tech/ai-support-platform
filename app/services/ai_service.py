import os
import json
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


def classify_ticket(text: str):

    prompt = f"""
    Classify the support ticket into exactly one category.
    
    Categories:
    - Payment Issue
    - Delivery Issue
    - Refund Request
    - Account Issue
    - Technical Issue
    - Other
    
    Ticket:
    
    {text}
    
    Return only the category name.
"""

    response = model.generate_content(prompt)

    return response.text.strip()


def analyze_ticket(text: str):

    prompt = f"""
    Analyze the following support conversation.

    Return ONLY valid JSON.

    Categories:
    - Payment Issue
    - Delivery Issue
    - Refund Request
    - Account Issue
    - Technical Issue
    - Other

    Sentiment:
    - Positive
    - Neutral
    - Negative

    Priority:
    - Low
    - Medium
    - High

    Conversation:

    {text}

    Return this format exactly:

    {{
        "summary": "...",
        "category": "...",
        "sentiment": "...",
        "priority": "..."
    }}

"""

    response = model.generate_content(prompt)

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned_response)

