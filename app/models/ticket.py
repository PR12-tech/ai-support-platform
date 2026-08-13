from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.db import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer,
                primary_key=True,
                index = True
    )

    ticket_id = Column(
        String,
        unique=True,
        nullable=False
    )

    title = Column(String,
                   nullable= False
    )

    description = Column(String,
                         nullable=False
    )

    status = Column(String,
                    default = "OPEN"
    )

    priority = Column(
        String,
        nullable=False
    )

    assigned_to = Column(
        String,
        nullable=False
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )