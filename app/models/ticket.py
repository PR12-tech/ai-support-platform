from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.db import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index = True)

    title = Column(String, nullable= False)

    description = Column(String, nullable=False)

    status = Column(String, default = "OPEN")

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )