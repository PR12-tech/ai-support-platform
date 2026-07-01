from evaluation.agent_evaluation import evaluate_agent


def run_evaluation(state):

    return evaluate_agent(

        question=state.question,

        tool_history=state.tool_history,

        context=state.context,

        answer=state.final_answer

    )