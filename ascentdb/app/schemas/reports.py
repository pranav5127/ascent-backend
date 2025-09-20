from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Dict, Any, Optional

class ReportsBase(BaseModel):
    student_id: UUID
    report: Dict[str, Any]
    summary: Dict[str, Any]

class ReportsCreate(ReportsBase):
    pass

class ReportsUpdate(BaseModel):
    report: Optional[Dict[str, Any]] = None
    summary: Optional[Dict[str, Any]] = None

class ReportsResponse(ReportsBase):
    id: UUID
    generated_at: datetime
    student_name: Optional[str] = None
    parent_mobile: Optional[str] = None

    class Config:
        orm_mode = True
