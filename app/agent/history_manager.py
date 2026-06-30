def tool_already_used(
        tool_history: list,
        tool_name: str
):

    used_tools = [
        item["tool"]
        for item in tool_history
    ]

    return tool_name in used_tools

def add_tool_history(
        tool_history: list,
        tool_name: str,
        arguments: dict,
        result: dict
):

    tool_history.append(
        {
            "tool": tool_name,

            "arguments": arguments,

            "result": result
        }
    )