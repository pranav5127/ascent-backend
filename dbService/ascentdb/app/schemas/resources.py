from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID
from typing import Optional

class ResourceBase(BaseModel):
    class_id: UUID
    title: str
    type: str
    description: Optional[str] = None
    file_url: Optional[str] = None
    due_date: Optional[date] = None
    created_at: Optional[datetime] = None

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
