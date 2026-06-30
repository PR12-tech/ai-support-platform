from app.agent.models import AgentResponse
from app.agent.state import AgentState
from app.agent.planner import choose_tool
from app.agent.preprocessor import preprocess_arguments
from app.agent.context_manager import update_context
from app.agent.observer import observe, add_observation
from app.agent.history_manager import tool_already_used, add_tool_history
from app.agent.constants import MAX_ITERATIONS
from app.logger import logger
from app.agent.executor import (
    execute_tool
)
from app.agent.response_generator import (
    generate_response
)



def run_agent(
        question: str
):

    state = AgentState(
        question=question
    )

    while state.iteration < MAX_ITERATIONS:

        tool_name, arguments = choose_tool(

            state.question,

            state.observations,

            state.tool_history,

            state.context
        )

        state.selected_tool = tool_name

        if tool_name == "NONE":

            break

        if tool_already_used(

            state.tool_history,

            tool_name

        ):

            print(f"{tool_name} was already used.")

            break

        arguments = preprocess_arguments(
            tool_name,
            arguments,
            state.context
        )

        result = execute_tool(

            tool_name,

            **arguments
        )

        state.tool_result = result

        update_context(
            state,
            tool_name,
            result
        )

        add_tool_history(

            state.tool_history,

            tool_name,

            arguments,

            result
        )

        decision = observe(

            state.question,

            tool_name,

            result,

            state.context

        )

        add_observation(

            state.observations,

            tool_name,

            arguments,

            result,

            decision

        )

        if decision == "FINISH":

            break

        elif decision == "CONTINUE":

            state.iteration += 1

            continue

        else:

            break

    answer = generate_response(

        state.question,

        state.selected_tool,

        state.tool_result

    )

    state.final_answer = answer

    return AgentResponse(

        tool=state.selected_tool,

        result=state.tool_result,

        answer=state.final_answer

    )
