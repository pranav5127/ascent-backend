from pydantic import BaseModel
from uuid import UUID

class SubjectBase(BaseModel):
    class_id: UUID
    name: str

class SubjectCreate(SubjectBase):
    pass

class SubjectResponse(SubjectBase):
    id: UUID

    model_config = {
        "from_attributes": True
    }
