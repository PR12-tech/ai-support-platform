from app.agent.prompts import OBSERVATION_PROMPT
from app.agent.utils import list_tools
from app.logger import logger
from app.services.ai_service import generate_content

def sanitize_for_observer(val):
    if isinstance(val, dict):
        new_dict = {}
        for k, v in val.items():
            if k == "chunks" and isinstance(v, list):
                new_dict[k] = f"<list of {len(v)} chunks>"
            elif k == "knowledge" and isinstance(v, str) and len(v) > 500:
                new_dict[k] = v[:500] + "... [truncated for observer context]"
            else:
                new_dict[k] = sanitize_for_observer(v)
        return new_dict
    elif isinstance(val, list):
        return [sanitize_for_observer(x) for x in val]
    return val


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

    sanitized_context = sanitize_for_observer(context)

    observation_prompt = OBSERVATION_PROMPT.format(

        question=question,

        tool=tool_name,

        result=observer_result,

        context=sanitized_context,

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

    # Allow the LLM to decide whether to continue or finish even after knowledge_search,
    # so that multi-tool queries can execute all necessary tools.
    # if (
    #         decision == "CONTINUE"
    #         and tool_name == "knowledge_search"
    #         and result.get("success")
    # ):
    #     logger.info(
    #         "Knowledge search completed successfully. Forcing FINISH."
    #     )
    #     return "FINISH"

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