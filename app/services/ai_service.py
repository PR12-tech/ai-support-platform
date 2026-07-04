import logging
import json

from app.logger import logger
from app.llm.provider_factory import get_provider


provider = get_provider()

logger = logging.getLogger(__name__)


def generate_content(prompt: str):

    response = provider.generate_content(
        prompt
    )

    if response is None:
        logger.error(
            "LLM provider returned an empty response."
        )

        return None

    return response

def summarize_text(text: str):

    prompt = f"""
    Summarize this following support conversation
    in 2-3 concise sentences:
    
    {text}
"""

    response = generate_content(prompt)

    if response is None:

        return "AI service temporarily unavailable."

    return response


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

    response = generate_content(prompt)

    if response is None:

        return "Other"

    return response.strip()


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

    response = generate_content(prompt)

    if response is None:

        return {
            "summary": "AI service temporarily unavailable.",
            "category": "Other",
            "sentiment": "Neutral",
            "priority": "Low"
        }

    cleaned_response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        return json.loads(cleaned_response)

    except json.JSONDecodeError:

        logger.exception("Failed to parse LLM JSON response.")

        return {
            "summary": "AI returned an invalid response.",
            "category": "Other",
            "sentiment": "Neutral",
            "priority": "Low"
        }
