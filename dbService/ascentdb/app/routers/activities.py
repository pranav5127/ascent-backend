from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from dbService.ascentdb.app.database import get_db
from dbService.ascentdb.app.schemas.activities import ActivitiesCreate, ActivitiesResponse
from dbService.ascentdb.app.crud.student_crud import create_activity, get_activities_by_student

router = APIRouter(prefix="/activities", tags=["Activities"])

@router.post("/", response_model=ActivitiesResponse)
def add_activity(activity: ActivitiesCreate, db: Session = Depends(get_db)):
    return create_activity(db, activity)

@router.get("/student/{student_id}", response_model=List[ActivitiesResponse])
def list_activities(student_id: str, db: Session = Depends(get_db)):
    return get_activities_by_student(db, student_id)
