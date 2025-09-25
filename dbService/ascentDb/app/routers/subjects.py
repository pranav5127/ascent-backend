from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ascentDb.app.crud.subjects import create_subject, get_subject, get_all_subjects, update_subject, delete_subject
from ascentDb.app.database import get_db
from ascentDb.app.schemas.subjects import SubjectCreate, SubjectResponse

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("/", response_model=SubjectResponse)
def create_subject_endpoint(sub: SubjectCreate, db: Session = Depends(get_db)):
    return create_subject(db, sub)

@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject_endpoint(subject_id: UUID, db: Session = Depends(get_db)):
    sub = get_subject(db, subject_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Subject not found")
    return sub

@router.get("/", response_model=List[SubjectResponse])
def get_all_subjects_endpoint(db: Session = Depends(get_db)):
    return get_all_subjects(db)

@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject_endpoint(subject_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    sub = update_subject(db, subject_id, update_data)
    if not sub:
        raise HTTPException(status_code=404, detail="Subject not found")
    return sub

@router.delete("/{subject_id}", response_model=SubjectResponse)
def delete_subject_endpoint(subject_id: UUID, db: Session = Depends(get_db)):
    sub = delete_subject(db, subject_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Subject not found")
    return sub
