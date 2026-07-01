from sqlalchemy import Column, Integer, String

from app.database.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(String, unique=True, nullable=False)

    customer = Column(String, nullable=False)

    status = Column(String, nullable=False)

    tracking_number = Column(String, nullable=True)

    estimated_delivery = Column(String, nullable=True)