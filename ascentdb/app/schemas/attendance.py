from pydantic import BaseModel
from uuid import UUID

class AttendanceBase(BaseModel):
    student_id: UUID
    month: str
    days_present: int = 0
    days_absent: int = 0

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(BaseModel):
    month: str | None
    days_present: int | None
    days_absent: int | None

class AttendanceResponse(AttendanceBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }