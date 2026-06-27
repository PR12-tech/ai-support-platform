from dataclasses import dataclass


@dataclass
class AgentState:

    question: str

    selected_tool: str = ""

    tool_result: dict | None = None

    final_answer: str = ""