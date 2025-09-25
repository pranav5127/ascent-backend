from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ProgressTrackingBase(BaseModel):
    student_id: UUID
    metric_type: str
    value: float
    recorded_at: datetime

class ProgressTrackingCreate(ProgressTrackingBase):
    pass

class ProgressTrackingResponse(ProgressTrackingBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }

class ClassProgressBase(BaseModel):
    class_id: UUID
    period: str
    avg_marks: float
    attendance_rate: float
    submission_rate: float
    created_at: datetime

class ClassProgressCreate(ClassProgressBase):
    pass

class ClassProgressResponse(ClassProgressBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
