def update_context(
        state,
        tool_name: str,
        result: dict
):

    CONTEXT_KEYS = {

        "order_lookup": "order",

        "ticket_lookup": "ticket",

        "knowledge_search": "knowledge",

        "send_email": "email",

        "sql_search": "sql"

    }

    key = CONTEXT_KEYS.get(
        tool_name
    )

    if key:

        state.context[key] = result