from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ascentDb.app.database import get_db
from ascentDb.app.schemas.attendance import AttendanceRecordBase, AttendanceRecordResponse, AttendanceMonthlyBase, AttendanceMonthlyResponse
from ascentDb.app.crud.attendance import add_attendance, get_attendance, get_attendance_by_class, add_attendance_monthly, get_attendance_monthly

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# Daily attendance
@router.post("/", response_model=AttendanceRecordResponse)
def add_attendance_endpoint(record: AttendanceRecordBase, db: Session = Depends(get_db)):
    return add_attendance(db, record)

@router.get("/{record_id}", response_model=AttendanceRecordResponse)
def get_attendance_endpoint(record_id: UUID, db: Session = Depends(get_db)):
    record = get_attendance(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    return record

@router.get("/class/{class_id}", response_model=List[AttendanceRecordResponse])
def get_attendance_by_class_endpoint(class_id: UUID, date: str = None, db: Session = Depends(get_db)):
    return get_attendance_by_class(db, class_id, date)

# Monthly attendance
@router.post("/monthly", response_model=AttendanceMonthlyResponse)
def add_attendance_monthly_endpoint(record: AttendanceMonthlyBase, db: Session = Depends(get_db)):
    return add_attendance_monthly(db, record)

@router.get("/monthly/{student_id}/{month}", response_model=AttendanceMonthlyResponse)
def get_attendance_monthly_endpoint(student_id: UUID, month: str, db: Session = Depends(get_db)):
    record = get_attendance_monthly(db, student_id, month)
    if not record:
        raise HTTPException(status_code=404, detail="Monthly attendance record not found")
    return record
