import json

from app.database.db import SessionLocal
from app.models.order import Order


def main():

    db = SessionLocal()

    with open(
        "data/orders.json",
        "r",
        encoding="utf-8"
    ) as file:

        orders = json.load(file)

    for order in orders:

        db.add(

            Order(

                order_id=order["order_id"],

                customer=order["customer"],

                status=order["status"],

                tracking_number=order["tracking_number"],

                estimated_delivery=order["estimated_delivery"]

            )

        )

    db.commit()

    db.close()

    print("Orders imported successfully.")


if __name__ == "__main__":

    main()