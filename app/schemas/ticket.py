from pydantic import BaseModel, ConfigDict


class TicketCreate(BaseModel):
    title: str
    description: str

class TicketCreateResponse(BaseModel):
    message: str

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)