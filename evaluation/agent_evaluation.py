from app.services.ai_service import model
from evaluation.models import AgentEvaluation
from evaluation.parser import parse_evaluation


def evaluate_agent(
        question: str,
        tool_history: list,
        context: dict,
        answer: str
):

    prompt = f"""
    You are an AI evaluator.

    Evaluate the customer support agent.

    User Question:

    {question}

    Tool History:

    {tool_history}

    Context:

    {context}

    Final Answer:

    {answer}

    Evaluate the following:

    1. Tool Selection (0-10)
    2. Groundedness (0-10)
    3. Completeness (0-10)
    4. Hallucination (True or False)
    5. Feedback

    Return ONLY valid JSON.
    """

    response = model.generate_content(
        prompt
    )

    return parse_evaluation(
        response.text
    )