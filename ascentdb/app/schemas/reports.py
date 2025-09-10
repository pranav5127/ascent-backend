from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Dict, Any

class ReportsBase(BaseModel):
    student_id: UUID
    report: Dict[str, Any]
    summary: Dict[str, Any]

class ReportsCreate(ReportsBase):
    pass

class ReportsUpdate(BaseModel):
    report: Dict[str, Any] | None
    summary: Dict[str, Any] | None

class ReportsResponse(ReportsBase):
    id: UUID
    generated_at: datetime

    class Config:
        orm_mode = True
