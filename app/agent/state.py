from dataclasses import dataclass, field


@dataclass
class AgentState:

    question: str

    selected_tool: str = ""

    tool_result: dict | None = None

    context: dict = field(
        default_factory=dict
    )

    tool_history: list = field(
        default_factory=list
    )

    observations: list = field(
        default_factory=list
    )

    iteration: int = 0

    final_answer: str = ""