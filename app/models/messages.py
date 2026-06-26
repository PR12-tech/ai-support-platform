from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.database.db import Base

class Message(Base):

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    content = Column(
        String,
        nullable=False
    )

    sender = Column(
        String,
        nullable=False
    )

    ticket_id = Column(
        Integer,
        ForeignKey("tickets.id"),
        nullable=True
    )

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )