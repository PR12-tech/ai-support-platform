from dataclasses import dataclass

@dataclass
class AgentResponse:

    tool: str

    result: dict

    answer: str