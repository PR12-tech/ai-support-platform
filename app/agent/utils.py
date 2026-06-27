from app.agent.registry import TOOLS


def list_tools():

    text = ""

    for tool_data in TOOLS.values():

        tool = tool_data["tool"]

        text += (
            f"Tool: {tool.name}\n"
        )

        text += (
            f"Description: {tool.description}\n"
        )

        text += "Parameters:\n"

        for name, description in tool_data["parameters"].items():

            text += (
                f"- {name}: {description}\n"
            )

        text += "\n"

    return text