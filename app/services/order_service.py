import json


with open(
        "data/orders.json",
        "r"
) as file:

    ORDERS = json.load(
        file
    )


def lookup_order(
        order_id: str
):

    for order in ORDERS:

        if order["order_id"] == order_id:

            return {

                "success": True,

                "order": order
            }

    return {

        "success": False,

        "message": "Order Not Found."

    }