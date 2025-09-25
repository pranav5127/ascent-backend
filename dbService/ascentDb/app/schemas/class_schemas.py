from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ClassBase(BaseModel):
    name: str
    teacher_id: UUID

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }

class ClassStudentBase(BaseModel):
    class_id: UUID
    student_id: UUID

class ClassStudentCreate(ClassStudentBase):
    pass

class ClassStudentResponse(ClassStudentBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
