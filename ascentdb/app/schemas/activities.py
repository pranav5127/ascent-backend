from pydantic import BaseModel
from uuid import UUID
from datetime import date

class ActivitiesBase(BaseModel):
    student_id: UUID
    activity_type: str
    description: str | None
    achievement: str | None
    date: date

class ActivitiesCreate(ActivitiesBase):
    pass

class ActivitiesUpdate(BaseModel):
    activity_type: str | None
    description: str | None
    achievement: str | None
    date: date | None

class ActivitiesResponse(ActivitiesBase):
    id: UUID

    class Config:
        orm_mode = True
