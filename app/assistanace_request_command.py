from pydantic import BaseModel

class AssistanceRequestCommand(BaseModel):
    topic: str
    description: str
