from app.services.ai_service import model
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
        context: str
):

    prompt = TOOL_SELECTION_PROMPT.format(

        tools=list_tools(),

        question=question,

        observations=observations,

        tool_history=tool_history,

        context=context

    )

    response = model.generate_content(
        prompt
    )

    logger.info("========== Gemini Raw Response ==========")
    logger.info(response.text)
    logger.info("========================================")

    tool_name, arguments = parse_tool_response(
        response.text
    )

    logger.info(
        f"Planner selected tool: {tool_name}"
        )

    logger.info(
        f"Planner arguments: {arguments}"
    )

    return tool_name, arguments