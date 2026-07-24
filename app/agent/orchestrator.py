from app.agent.models import AgentResponse
from app.agent.state import AgentState
from app.agent.planner import choose_tool
from app.agent.preprocessor import preprocess_arguments
from app.agent.context_manager import update_context
from app.agent.observer import observe, add_observation
from app.agent.history_manager import tool_already_used, add_tool_history
from app.services.memory_service import add_message, get_history
from app.logger import logger
from app.agent.executor import (
    execute_tool
)
from app.agent.response_generator import (
    generate_response
)

MAX_ITERATIONS = 5

def run_agent(
        question: str,
        session_id: str
):

    state = AgentState(
        question=question
    )

    state.conversation_history = get_history(
        session_id
    )

    add_message(

        session_id=session_id,

        role="user",

        content=question
    )

    while state.iteration < MAX_ITERATIONS:

        tool_name, arguments = choose_tool(

            state.question,

            state.observations,

            state.tool_history,

            state.context,

            state.conversation_history
        )

        state.selected_tool = tool_name

        if tool_name == "NONE":

            if state.tool_history:
                break

            state.final_answer = (
                "I'm sorry, I couldn't process your request at the moment."
            )

            add_message(
                session_id=session_id,
                role="assistant",
                content=state.final_answer
            )

            return AgentResponse(
                tools_used=[],
                answer=state.final_answer
            )

        if tool_already_used(

            state.tool_history,

            tool_name

        ):

            logger.warning(
                "%s was already used.",
                tool_name
            )

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

        state.context
    )

    state.final_answer = answer

    add_message(

        session_id=session_id,

        role="assistant",

        content=state.final_answer
    )

    return AgentResponse(
        tools_used=state.tool_history,
        answer=answer
    )
