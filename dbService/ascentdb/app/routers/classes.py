from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ascentdb.app.crud.classes import create_class, get_class, get_all_classes, update_class, delete_class, \
    add_student_to_class, remove_student_from_class, get_students_in_class
from ascentdb.app.database import get_db
from ascentdb.app.schemas.class_schemas import ClassResponse, ClassCreate, ClassStudentResponse, ClassStudentCreate

router = APIRouter(prefix="/classes", tags=["Classes"])

# Class endpoints
@router.post("/", response_model=ClassResponse)
def create_class_endpoint(cls: ClassCreate, db: Session = Depends(get_db)):
    return create_class(db, cls)

@router.get("/{class_id}", response_model=ClassResponse)
def get_class_endpoint(class_id: UUID, db: Session = Depends(get_db)):
    cls = get_class(db, class_id)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    return cls

@router.get("/", response_model=List[ClassResponse])
def get_all_classes_endpoint(db: Session = Depends(get_db)):
    return get_all_classes(db)

@router.put("/{class_id}", response_model=ClassResponse)
def update_class_endpoint(class_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    cls = update_class(db, class_id, update_data)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    return cls

@router.delete("/{class_id}", response_model=ClassResponse)
def delete_class_endpoint(class_id: UUID, db: Session = Depends(get_db)):
    cls = delete_class(db, class_id)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    return cls

# ClassStudent endpoints
@router.post("/students", response_model=ClassStudentResponse)
def add_student_endpoint(student: ClassStudentCreate, db: Session = Depends(get_db)):
    return add_student_to_class(db, student)

@router.delete("/students", response_model=ClassStudentResponse)
def remove_student_endpoint(student_id: UUID, class_id: UUID, db: Session = Depends(get_db)):
    result = remove_student_from_class(db, student_id, class_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found in class")
    return result

@router.get("/{class_id}/students", response_model=List[ClassStudentResponse])
def get_students_in_class_endpoint(class_id: UUID, db: Session = Depends(get_db)):
    students = get_students_in_class(db, class_id)
    if not students:
        raise HTTPException(status_code=404, detail="No students found in this class")
    return students
