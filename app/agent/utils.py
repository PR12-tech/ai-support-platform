from app.agent.registry import TOOLS


def list_tools():

    lines = []

    for tool_name, tool_data in TOOLS.items():

        tool = tool_data["tool"]

        lines.append(
            f"Tool: {tool.name}"
        )

        lines.append(
            f"Description: {tool.description}"
        )

        lines.append(
            "Parameters:"
        )

        for name, description in tool_data["parameters"].items():

            lines.append(
                f"- {name}: {description}"
            )

        lines.append("")

    return "\n".join(lines)