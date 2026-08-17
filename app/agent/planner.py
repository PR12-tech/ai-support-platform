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


def sanitize_for_planner(val):
    if isinstance(val, dict):
        new_dict = {}
        for k, v in val.items():
            if k == "knowledge" and isinstance(v, str) and len(v) > 150:
                new_dict[k] = v[:150] + "... [truncated for planner]"
            elif k == "chunks" and isinstance(v, list):
                new_dict[k] = f"<list of {len(v)} chunks>"
            else:
                new_dict[k] = sanitize_for_planner(v)
        return new_dict
    elif isinstance(val, list):
        return [sanitize_for_planner(x) for x in val]
    return val


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

    sanitized_observations = sanitize_for_planner(observations)
    sanitized_tool_history = sanitize_for_planner(tool_history)
    sanitized_context = sanitize_for_planner(context)

    prompt = TOOL_SELECTION_PROMPT.format(

        tools=list_tools(),

        conversation_history=history_text,

        question=question,

        observations=sanitized_observations,

        tool_history=sanitized_tool_history,

        context=sanitized_context

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