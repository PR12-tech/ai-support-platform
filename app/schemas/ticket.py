from pydantic import BaseModel, ConfigDict


class TicketCreate(BaseModel):
    title: str
    description: str

class TicketCreateResponse(BaseModel):
    message: str

class TicketResponse(BaseModel):
    id: int
    ticket_id: str
    title: str
    description: str
    status: str
    priority: str
    assigned_to: str | None
    owner_id: int

    model_config = ConfigDict(from_attributes=True)