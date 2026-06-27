from app.agent.errors import ToolNotFoundError
from app.agent.registry import TOOLS



def execute_tool(
        tool_name: str,
        **kwargs
):

    tool = TOOLS.get(
        tool_name
    )

    if not tool:

        raise ToolNotFoundError(
            tool_name
        )


    return tool["tool"].execute(
        **kwargs
    )