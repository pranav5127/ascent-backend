from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Dict, Any

class MarksBase(BaseModel):
    student_id: UUID
    exam_type: str
    subject_scores: Dict[str, Any]
    teacher_note: str | None
    date: date

class MarksCreate(MarksBase):
    pass

class MarksUpdate(BaseModel):
    exam_type: str | None
    subject_scores: Dict[str, Any] | None
    teacher_note: str | None
    date: date | None

class MarksResponse(MarksBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }