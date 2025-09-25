from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class NotificationBase(BaseModel):
    recipient_id: UUID
    class_id: UUID
    type: str
    message: str
    created_at: datetime
    read: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
