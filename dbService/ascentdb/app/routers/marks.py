from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dbService.ascentdb.app.database import get_db
from dbService.ascentdb.app.schemas.marks import MarksCreate, MarksResponse
from dbService.ascentdb.app.crud.student_crud import  create_marks, get_marks_by_student

router = APIRouter(prefix="/marks", tags=["Marks"])

@router.post("/", response_model=MarksResponse)
def add_marks(marks: MarksCreate, db: Session = Depends(get_db)):
    return create_marks(db, marks)

@router.get("/student/{student_id}", response_model=List[MarksResponse])
def list_marks(student_id: str, db: Session = Depends(get_db)):
    return get_marks_by_student(db, student_id)
