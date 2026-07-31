from pydantic import BaseModel, ConfigDict

class MessageCreate(BaseModel):
    content:str

class MessageCreateResponse(BaseModel):
    message: str

class MessageResponse(BaseModel):
    id: int
    content: str
    sender: str
    ticket_id: int

    model_config = ConfigDict(from_attributes=True)

class TicketSummaryResponse(BaseModel):
    ticket_id: int
    conversation: str
    summary: str

class TicketClassificationResponse(BaseModel):
    ticket_id: int
    category: str

class TicketAnalysisResponse(BaseModel):
    summary: str
    category: str
    sentiment: str
    priority: str