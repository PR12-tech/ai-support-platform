from app.agent.prompts import OBSERVATION_PROMPT
from app.agent.utils import list_tools
from app.logger import logger
from app.services.ai_service import generate_content

def observe(
        question: str,
        tool_name: str,
        result: dict,
        context: dict
):

    observer_result = result

    if tool_name == "knowledge_search":
        observer_result = {
            "success": result.get("success"),
            "knowledge": result.get("data", {}).get("knowledge", ""),
            "sources": result.get("data", {}).get("sources", [])
        }

    observation_prompt = OBSERVATION_PROMPT.format(

        question=question,

        tool=tool_name,

        result=observer_result,

        context=context,

        tools=list_tools()

    )

    response = generate_content(
        observation_prompt
    )

    if response is None:

        logger.warning(
            "Observer unavailable. Defaulting to FINISH."
        )

        return "FINISH"

    logger.debug(
        f"Observer raw response:\n{response}"
    )

    decision = response.strip().split()[0].upper()

    if (
            decision == "CONTINUE"
            and tool_name == "knowledge_search"
            and result.get("success")
    ):
        logger.info(
            "Knowledge search completed successfully. Forcing FINISH."
        )
        return "FINISH"

    logger.info(
        f"Observer decision: {decision}"
    )

    return decision

def add_observation(
        observations: list,
        tool_name: str,
        arguments: dict,
        result: dict,
        decision: str
):

    observations.append(
        {
            "tool": tool_name,

            "arguments": arguments,

            "result": result,

            "decision": decision
        }
    )

    logger.info(
        "Observation added to history."
    )