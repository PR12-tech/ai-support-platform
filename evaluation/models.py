from dataclasses import dataclass


@dataclass
class AgentEvaluation:

    tool_selection: int

    groundedness: int

    completeness: int

    hallucination: bool

    feedback: str


