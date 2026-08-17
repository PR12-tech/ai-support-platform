def is_similar_sql_question(q1: str, q2: str) -> bool:
    w1 = set(q1.lower().split())
    w2 = set(q2.lower().split())
    if not w1 or not w2:
        return q1.lower() == q2.lower()
    intersection = w1.intersection(w2)
    union = w1.union(w2)
    return len(intersection) / len(union) >= 0.75


def tool_already_used(
        tool_history: list,
        tool_name: str,
        arguments: dict
):

    # Check exact match first
    if any(
        item["tool"] == tool_name
        and item["arguments"] == arguments
        for item in tool_history
    ):
        return True

    # Check for failed sql_search with highly similar questions to prevent retry loops
    if tool_name == "sql_search" and "question" in arguments:
        new_q = arguments["question"]
        for item in tool_history:
            if (
                item["tool"] == "sql_search"
                and not item.get("result", {}).get("success", True)
            ):
                prev_q = item["arguments"].get("question", "")
                if is_similar_sql_question(prev_q, new_q):
                    return True

    return False

def add_tool_history(
        tool_history: list,
        tool_name: str,
        arguments: dict,
        result: dict
):

    tool_history.append(
        {
            "tool": tool_name,

            "arguments": arguments,

            "result": result
        }
    )