from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.order import Order
from app.models.user import User


def lookup_order(order_id, user_id):

    db: Session = SessionLocal()

    try:
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "Order not found."
            }

        order = (
            db.query(Order)
            .filter(
                Order.order_id == order_id,
                func.lower(Order.customer) == func.lower(user.username)
            )
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