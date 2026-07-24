from dataclasses import dataclass

@dataclass
class AgentResponse:

    tools_used: list[str]

    answer: str