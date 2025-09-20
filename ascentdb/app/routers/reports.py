from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ascentdb.app.database import get_db
from ascentdb.app.schemas.reports import ReportsCreate, ReportsResponse
from ascentdb.app.crud.student_crud import create_or_update_report, get_reports_by_student

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/", response_model=ReportsResponse)
def add_or_update_report(report: ReportsCreate, db: Session = Depends(get_db)):
    db_report = create_or_update_report(db, report)
    if not db_report:
        raise HTTPException(status_code=400, detail="Failed to create or update report")
    return db_report

@router.put("/", response_model=ReportsResponse)
def edit_report(report: ReportsCreate, db: Session = Depends(get_db)):
    db_report = create_or_update_report(db, report)
    if not db_report:
        raise HTTPException(status_code=400, detail="Failed to update report")
    return db_report

@router.get("/student/{student_id}", response_model=ReportsResponse)
def get_report(student_id: str, db: Session = Depends(get_db)):
    db_report = get_reports_by_student(db, student_id)
    if not db_report:
        raise HTTPException(status_code=404, detail="No report found for this student")
    return db_report
