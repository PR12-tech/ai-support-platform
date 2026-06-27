from app.agent.executor import execute_tool
from app.agent.parser import parse_tool_response
from app.agent.prompts import TOOL_SELECTION_PROMPT, OBSERVATION_PROMPT
from app.agent.utils import list_tools
from app.services.ai_service import model


def run_react(
        question: str
):

    prompt =TOOL_SELECTION_PROMPT.format(

        tools=list_tools(),

        question=question
    )

    response = model.generate_content(
        prompt
    )

    tool_name, arguments = parse_tool_response(
        response.text
    )

    result = execute_tool(

        tool_name,

        **arguments
    )

    observation_prompt = OBSERVATION_PROMPT.format(

        question=question,

        tool=tool_name,

        result=result
    )

    observation = model.generate_content(

        observation_prompt

    )

    decision = observation.text.strip()

    print("\nDecision:")

    print(decision)

    return result