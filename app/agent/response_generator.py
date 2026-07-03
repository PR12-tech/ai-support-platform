from app.services.ai_service import generate_content
from app.agent.response_builders import (
    build_order_response,
    build_ticket_response,
    build_sql_response
)

def generate_response(
        question: str,
        tool_name: str,
        tool_result: dict
):

    if tool_name == "order_lookup":

        return build_order_response(tool_result)

    if tool_name == "ticket_lookup":

        return build_ticket_response(tool_result)

    if tool_name == "sql_search":

        return build_sql_response(tool_result)


    prompt = f"""
    You are a helpful AI customer support assistant.

    The user's question:

    {question}

    The selected tool:

    {tool_name}

    Tool result:

    {tool_result}

    Using ONLY the tool result, answer the user's question naturally.

    If the tool returned an error, explain it politely.
    """

    response = generate_content(
        prompt
    )

    return response