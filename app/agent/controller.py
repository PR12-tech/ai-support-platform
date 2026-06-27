from torchgen.api.cpp import arguments

from app.services.ai_service import model

from app.agent.prompts import (
    TOOL_SELECTION_PROMPT
)

from app.agent.executor import (
    execute_tool
)

from app.agent.utils import (
    list_tools
)

from app.agent.models import AgentResponse

from app.agent.response_generator import (
    generate_response
)

from app.agent.parser import (
    parse_tool_response
)

def run_agent(
        question: str
):

    prompt = TOOL_SELECTION_PROMPT.format(

        tools=list_tools(),

        question=question
    )

    response = model.generate_content(
        prompt
    )

    print("\n========== Gemini Raw Response ==========\n")
    print(response.text)
    print("\n=========================================\n")

    tool_name, arguments = parse_tool_response(
        response.text
    )

    if tool_name == "NONE":

        return AgentResponse(

        tool="none",

        result={},

        answer="I couldn't determine the correct tool."
        )

    result = execute_tool(

        tool_name,

        **arguments
    )

    answer = generate_response(
        question,
        tool_name,
        result
    )


    return AgentResponse(

        tool=tool_name,

        result=result,

        answer=answer
    )