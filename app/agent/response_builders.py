def build_order_response(result: dict):

    if not result["success"]:

        return result["message"]

    order = result["data"]["order"]

    return (
        f"Order ID: {order['order_id']}\n"
        f"Customer: {order['customer']}\n"
        f"Status: {order['status']}\n"
        f"Tracking Number: {order['tracking_number']}\n"
        f"Estimated Delivery: {order['estimated_delivery']}"
    )


def build_ticket_response(result: dict):

    if not result["success"]:

        return result["message"]

    ticket = result["data"]["ticket"]

    return (
        f"Ticket ID: {ticket['ticket_id']}\n"
        f"Customer: {ticket['customer']}\n"
        f"Status: {ticket['status']}\n"
        f"Priority: {ticket['priority']}\n"
        f"Assigned To: {ticket['assigned_to']}"
    )


def build_sql_response(result: dict):

    if not result["success"]:

        return result["message"]

    rows = result["data"]

    if not rows:

        return "No matching records found."

    return str(rows)
