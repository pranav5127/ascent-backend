from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ReportBase(BaseModel):
    student_id: UUID
    class_id: UUID
    period: str
    report_text: str
    created_at: datetime

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
