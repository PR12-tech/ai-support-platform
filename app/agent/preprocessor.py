from app.agent.email_builder import build_email


def preprocess_arguments(
        tool_name: str,
        arguments: dict,
        context: dict
):

    if tool_name == "send_email":

        email = build_email(
            context
        )

        arguments["subject"] = email["subject"]

        arguments["body"] = email["body"]

    return arguments