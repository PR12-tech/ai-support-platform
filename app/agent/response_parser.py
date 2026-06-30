import json
from app.logger import logger


def parse_tool_response(
        response: str
):

    response = response.strip()

    if response.startswith("```json"):

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

    elif response.startswith("```"):

        response = response.replace(
            "```",
            ""
        )

    response = response.strip()

    try:
        data = json.loads(
            response
        )

    except json.JSONDecodeError:

        logger.exception(
            "Planner returned invalid JSON"
        )

        raise

    tool_name = data.get("tool")

    arguments = data.get("arguments", {})

    return tool_name, arguments