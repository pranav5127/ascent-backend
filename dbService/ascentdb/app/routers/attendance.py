from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dbService.ascentdb.app.database import get_db
from dbService.ascentdb.app.schemas.attendance import AttendanceCreate, AttendanceResponse
from dbService.ascentdb.app.crud.student_crud import create_attendance, get_attendance_by_student

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=AttendanceResponse)
def add_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    return create_attendance(db, attendance)

@router.get("/student/{student_id}", response_model=List[AttendanceResponse])
def list_attendance(student_id: str, db: Session = Depends(get_db)):
    return get_attendance_by_student(db, student_id)
