from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ascentdb.app.database import get_db
from ascentdb.app.schemas.reports import ReportBase, ReportResponse
from ascentdb.app.crud.reports import create_report, get_report, get_reports_by_student, update_report, delete_report

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/", response_model=ReportResponse)
def create_report_endpoint(report: ReportBase, db: Session = Depends(get_db)):
    return create_report(db, report)

@router.get("/{report_id}", response_model=ReportResponse)
def get_report_endpoint(report_id: UUID, db: Session = Depends(get_db)):
    r = get_report(db, report_id)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    return r

@router.get("/student/{student_id}", response_model=List[ReportResponse])
def get_reports_by_student_endpoint(student_id: UUID, db: Session = Depends(get_db)):
    return get_reports_by_student(db, student_id)

@router.put("/{report_id}", response_model=ReportResponse)
def update_report_endpoint(report_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    r = update_report(db, report_id, update_data)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    return r

@router.delete("/{report_id}", response_model=ReportResponse)
def delete_report_endpoint(report_id: UUID, db: Session = Depends(get_db)):
    r = delete_report(db, report_id)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    return r
