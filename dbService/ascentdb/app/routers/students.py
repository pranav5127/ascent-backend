from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dbService.ascentdb.app.database import get_db
from dbService.ascentdb.app.schemas.student import StudentCreate, StudentResponse
from dbService.ascentdb.app.crud.student_crud import create_student, get_students, get_student

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@router.get("/", response_model=List[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.get("/{student_id}", response_model=StudentResponse)
def retrieve_student(student_id: str, db: Session = Depends(get_db)):
    return get_student(db, student_id)
