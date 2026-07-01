from sqlalchemy import Column, Integer, String

from app.database.db import Base


class SupportTicket(Base):

    __tablename__ = "support_tickets"

    id = Column(Integer, primary_key=True, index=True)

    ticket_id = Column(String, unique=True, nullable=False)

    customer = Column(String, nullable=False)

    status = Column(String, nullable=False)

    priority = Column(String, nullable=False)

    assigned_to = Column(String, nullable=False)