from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ascentDb.app.database import get_db
from ascentDb.app.schemas.exams import (
    ExamCreate, ExamResponse,
    ExamMarkBase, ExamMarkResponse
)
from ascentDb.app.crud.exams import (
    create_exam, get_exam, get_all_exams,
    update_exam, delete_exam,
    add_exam_mark, get_exam_marks
)

router = APIRouter(prefix="/exams", tags=["Exams"])

@router.post("/", response_model=ExamResponse)
def create_exam_endpoint(exam: ExamCreate, db: Session = Depends(get_db)):
    return create_exam(db, exam)


@router.get("/{exam_id}", response_model=ExamResponse)
def get_exam_endpoint(exam_id: UUID, db: Session = Depends(get_db)):
    exam = get_exam(db, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@router.get("/", response_model=List[ExamResponse])
def get_all_exams_endpoint(db: Session = Depends(get_db)):
    return get_all_exams(db)


@router.put("/{exam_id}", response_model=ExamResponse)
def update_exam_endpoint(exam_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    exam = update_exam(db, exam_id, update_data)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam


@router.delete("/{exam_id}", response_model=ExamResponse)
def delete_exam_endpoint(exam_id: UUID, db: Session = Depends(get_db)):
    exam = delete_exam(db, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam

@router.post("/marks", response_model=ExamMarkResponse)
def add_exam_mark_endpoint(mark: ExamMarkBase, db: Session = Depends(get_db)):
    try:
        return add_exam_mark(db, mark)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{exam_id}/marks", response_model=List[ExamMarkResponse])
def get_exam_marks_endpoint(exam_id: UUID, db: Session = Depends(get_db)):
    return get_exam_marks(db, exam_id)
