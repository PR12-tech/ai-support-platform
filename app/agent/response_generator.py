from app.services.ai_service import generate_content
from app.agent.response_builders import (
    build_order_response,
    build_ticket_response,
    build_sql_response
)

def generate_response(
        question: str,
        context: dict
):

    prompt = f"""
    You are a helpful AI customer support assistant.

    The user's question:

    {question}

    Collected Context:

    {context}
    
    Using ONLY the collected context above, answer the user's question.
    
    Rules:
    - Use all information present in the collected context
    - If multiple tools contributed information, combine it into one natural answer.
    - Do not say information is unavailable if it exists in the collected context.
    - Do not invent information that is not present in the collected context.
    - If the collected context contains an error, explain it politely.
"""

    response = generate_content(
        prompt
    )

    if response is None:
        return "AI service temporarily unavailable. Please try again in a few moments."

    return response