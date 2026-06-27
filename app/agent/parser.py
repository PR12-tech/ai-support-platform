import json


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

    data = json.loads(
        response
    )

    tool_name = data["tool"]

    arguments = data["arguments"]

    return tool_name, arguments