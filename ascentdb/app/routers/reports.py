from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ascentdb.app.database import get_db
from ascentdb.app.schemas.reports import ReportsCreate, ReportsResponse
from ascentdb.app.crud.student_crud import create_report, get_reports_by_student

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/", response_model=ReportsResponse)
def add_report(report: ReportsCreate, db: Session = Depends(get_db)):
    return create_report(db, report)

@router.get("/student/{student_id}", response_model=List[ReportsResponse])
def list_reports(student_id: str, db: Session = Depends(get_db)):
    return get_reports_by_student(db, student_id)
