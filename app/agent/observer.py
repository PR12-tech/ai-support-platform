from app.services.ai_service import model
from app.agent.prompts import OBSERVATION_PROMPT
from app.agent.utils import list_tools
from app.logger import logger


def observe(
        question: str,
        tool_name: str,
        result: dict,
        context: dict
):

    observation_prompt = OBSERVATION_PROMPT.format(

        question=question,

        tool=tool_name,

        result=result,

        context=context,

        tools=list_tools()

    )

    response = model.generate_content(
        observation_prompt
    )

    decision = response.text.strip()

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