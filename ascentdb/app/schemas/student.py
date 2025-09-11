from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class StudentBase(BaseModel):
    name: str
    class_name: str
    parent_id: UUID

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None
    class_name: str | None
    parent_id: UUID | None

class StudentResponse(StudentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    } # Lets Pydantic read orm objects directly.