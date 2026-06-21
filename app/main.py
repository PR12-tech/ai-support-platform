from fastapi import FastAPI

from app.database.db import engine
from app.models.user import User
from app.database.db import Base
from app.api.auth import router as auth_router
from app.models.ticket import Ticket
from app.api.tickets import router as ticket_router
from app.models.messages import Message
from app.api.messages import router as message_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

app.include_router(ticket_router)

app.include_router(message_router)

@app.get("/")
def home():
    return {"message": "AI Support Platform"}