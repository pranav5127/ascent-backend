from pydantic import BaseModel

class MessageData(BaseModel):
    from_: str
    body: str
    to: str
