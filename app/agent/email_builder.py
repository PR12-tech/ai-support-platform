def build_email(
        context: dict
):

    subject = "Customer Support Update"

    lines = []

    order = context.get("order")

    if order and order.get("success"):

        data = order["data"]["order"]

        lines.append("Order Information:")
        lines.append(f"Order ID: {data['order_id']}")
        lines.append(f"Status: {data['status']}")

        if "tracking_number" in data:

            lines.append(
                f"Tracking Number: {data['tracking_number']}"
            )

        lines.append("")

    ticket = context.get("ticket")

    if ticket and ticket.get("success"):

        data = ticket["data"]["ticket"]

        lines.append("Ticket Information:")
        lines.append(f"Ticket ID: {data['ticket_id']}")
        lines.append(f"Status: {data['status']}")
        lines.append(f"Priority: {data['priority']}")
        lines.append(f"Assigned To: {data['assigned_to']}")
        lines.append("")

    knowledge = context.get("knowledge")

    if knowledge:

        lines.append("Support Information:")

        lines.append(
            knowledge["data"]["knowledge"]
        )

        lines.append("")

        if knowledge["data"].get("sources"):
            lines.append(
                "Sources: "
                + ", ".join(
                    knowledge["data"]["sources"]
                )
            )

            lines.append("")

    body = "\n".join(lines)

    return {

        "subject": subject,

        "body": body

    }