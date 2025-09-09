from pydantic import BaseModel

class ApiData(BaseModel):
    sender_contact: str
    message_text: str
    receiver_contact: str

