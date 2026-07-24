from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.order import Order


def lookup_order(order_id):

    db: Session = SessionLocal()

    try:
        order = (
            db.query(Order)
            .filter(Order.order_id == order_id)
            .first()
        )

        if not order:
            return {
                "success": False,
                "message": "Order not found."
            }

        return {
            "success": True,
            "order": {
                "id": order.id,
                "order_id": order.order_id,
                "customer": order.customer,
                "status": order.status,
                "tracking_number": order.tracking_number,
                "estimated_delivery": order.estimated_delivery
            }
        }

    finally:
        db.close()