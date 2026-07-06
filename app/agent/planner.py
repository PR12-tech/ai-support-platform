from app.services.ai_service import generate_content
from app.logger import logger

from app.agent.prompts import (
    TOOL_SELECTION_PROMPT
)

from app.agent.response_parser import (
    parse_tool_response
)

from app.agent.utils import (
    list_tools
)


def choose_tool(
        question: str,
        observations: list,
        tool_history: list,
        context: dict,
        conversation_history: list
):

    history_text = "\n".join(

        f"{message['role']}: {message['content']}"

        for message in conversation_history
    )

    prompt = TOOL_SELECTION_PROMPT.format(

        tools=list_tools(),

        conversation_history=history_text,

        question=question,

        observations=observations,

        tool_history=tool_history,

        context=context

    )

    response = generate_content(prompt)

    if response is None:

        logger.error(
            "Planner failed because the AI service is unavailable."
        )

        return "NONE", {}

    logger.info("========== Planner Raw Response ==========")
    logger.info(response)
    logger.info("========================================")

    tool_name, arguments = parse_tool_response(
        response
    )

    logger.info(
        f"Planner selected tool: {tool_name}"
        )

    logger.info(
        f"Planner arguments: {arguments}"
    )

    return tool_name, arguments