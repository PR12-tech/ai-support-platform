def tool_already_used(
        tool_history: list,
        tool_name: str,
        arguments: dict
):

    return any(
        item["tool"] == tool_name
        and item["arguments"] == arguments
        for item in tool_history
    )

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