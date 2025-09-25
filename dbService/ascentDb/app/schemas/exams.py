from pydantic import BaseModel
from datetime import date
from uuid import UUID

class ExamBase(BaseModel):
    class_id: UUID
    name: str
    date: date

class ExamCreate(ExamBase):
    pass

class ExamResponse(ExamBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }

class ExamMarkBase(BaseModel):
    exam_id: UUID
    student_id: UUID
    subject_id: UUID
    marks: int

class ExamMarkCreate(ExamMarkBase):
    pass

class ExamMarkResponse(ExamMarkBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
