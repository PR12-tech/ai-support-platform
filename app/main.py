from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.request_middleware import request_id_middleware
from app.database.db import engine
from app.models.user import User
from app.database.db import Base
from app.api.auth import router as auth_router
from app.models.ticket import Ticket
from app.api.tickets import router as ticket_router
from app.models.messages import Message
from app.api.messages import router as message_router
from app.api.rag import router as rag_router
from app.core.exception_handlers import register_exception_handlers
from app.api.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield

    # Future cleanup code goes here

app = FastAPI(
    lifespan=lifespan
)

app.middleware("http")(request_id_middleware)

register_exception_handlers(app)

app.include_router(auth_router)

app.include_router(ticket_router)

app.include_router(message_router)

app.include_router(rag_router)

app.include_router(health_router)



@app.get("/")
def home():
    return {"message": "AI Support Platform"}

