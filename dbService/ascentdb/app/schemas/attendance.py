from pydantic import BaseModel
from datetime import date
from uuid import UUID

class AttendanceRecordBase(BaseModel):
    student_id: UUID
    class_id: UUID
    date: date
    status: str  # present, absent, late

class AttendanceRecordCreate(AttendanceRecordBase):
    pass

class AttendanceRecordResponse(AttendanceRecordBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }

class AttendanceMonthlyBase(BaseModel):
    student_id: UUID
    class_id: UUID
    month: str
    present_days: int
    absent_days: int
    late_days: int

class AttendanceMonthlyCreate(AttendanceMonthlyBase):
    pass

class AttendanceMonthlyResponse(AttendanceMonthlyBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
