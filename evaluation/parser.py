import json

from evaluation.models import AgentEvaluation

def parse_evaluation(
        response: str
):

    response = response.strip()

    if response.startswith("```json"):

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

    elif response.startswith("```"):

        response = response.replace(
            "```",
            ""
        )

    response = response.strip()

    data = json.loads(
        response
    )

    return AgentEvaluation(

        tool_selection=data["tool_selection"],

        groundedness=data["groundedness"],

        completeness=data["completeness"],

        hallucination=data["hallucination"],

        feedback=data["feedback"]

    )