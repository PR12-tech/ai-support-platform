def update_context(
        state,
        tool_name: str,
        result: dict
):

    if tool_name == "order_lookup":

        state.context["order"] = result

    elif tool_name == "ticket_lookup":

        state.context["ticket"] = result

    elif tool_name == "knowledge_search":

        state.context["knowledge"] = result

    elif tool_name == "send_email":

        state.context["email"] = result