from app.agent.errors import ToolNotFoundError
from app.agent.registry import TOOLS
from app.logger import logger


def execute_tool(
        tool_name: str,
        **kwargs
):

    logger.info(
        f"Executing tool: {tool_name}"
    )

    tool = TOOLS.get(
        tool_name
    )

    if not tool:

        raise ToolNotFoundError(
            tool_name
        )

    try:

        result = tool["tool"].execute(
            **kwargs
        )

        logger.info(
            f"Tool execution completed: {tool_name}"
        )

        return result

    except Exception:

        logger.exception(
            f"Tool execution failed: {tool_name}"
        )

        raise