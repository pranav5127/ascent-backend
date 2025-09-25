from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ascentDb.app.database import get_db
from ascentDb.app.schemas.progress import ProgressTrackingBase, ProgressTrackingResponse, ClassProgressBase, ClassProgressResponse
from ascentDb.app.crud.progress import add_progress, get_progress, get_all_progress, update_progress, delete_progress, add_class_progress, get_class_progress, get_all_class_progress, update_class_progress, delete_class_progress

router = APIRouter(prefix="/progress", tags=["Progress"])

# ProgressTracking endpoints
@router.post("/", response_model=ProgressTrackingResponse)
def add_progress_endpoint(progress: ProgressTrackingBase, db: Session = Depends(get_db)):
    return add_progress(db, progress)

@router.get("/{progress_id}", response_model=ProgressTrackingResponse)
def get_progress_endpoint(progress_id: UUID, db: Session = Depends(get_db)):
    record = get_progress(db, progress_id)
    if not record:
        raise HTTPException(status_code=404, detail="Progress record not found")
    return record

@router.get("/", response_model=List[ProgressTrackingResponse])
def get_all_progress_endpoint(db: Session = Depends(get_db)):
    return get_all_progress(db)

@router.put("/{progress_id}", response_model=ProgressTrackingResponse)
def update_progress_endpoint(progress_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    record = update_progress(db, progress_id, update_data)
    if not record:
        raise HTTPException(status_code=404, detail="Progress record not found")
    return record

@router.delete("/{progress_id}", response_model=ProgressTrackingResponse)
def delete_progress_endpoint(progress_id: UUID, db: Session = Depends(get_db)):
    record = delete_progress(db, progress_id)
    if not record:
        raise HTTPException(status_code=404, detail="Progress record not found")
    return record

# ClassProgress endpoints
@router.post("/class", response_model=ClassProgressResponse)
def add_class_progress_endpoint(progress: ClassProgressBase, db: Session = Depends(get_db)):
    return add_class_progress(db, progress)

@router.get("/class/{class_id}/{period}", response_model=ClassProgressResponse)
def get_class_progress_endpoint(class_id: UUID, period: str, db: Session = Depends(get_db)):
    record = get_class_progress(db, class_id, period)
    if not record:
        raise HTTPException(status_code=404, detail="Class progress not found")
    return record

@router.get("/class", response_model=List[ClassProgressResponse])
def get_all_class_progress_endpoint(db: Session = Depends(get_db)):
    return get_all_class_progress(db)

@router.put("/class/{progress_id}", response_model=ClassProgressResponse)
def update_class_progress_endpoint(progress_id: UUID, update_data: dict, db: Session = Depends(get_db)):
    record = update_class_progress(db, progress_id, update_data)
    if not record:
        raise HTTPException(status_code=404, detail="Class progress not found")
    return record

@router.delete("/class/{progress_id}", response_model=ClassProgressResponse)
def delete_class_progress_endpoint(progress_id: UUID, db: Session = Depends(get_db)):
    record = delete_class_progress(db, progress_id)
    if not record:
        raise HTTPException(status_code=404, detail="Class progress not found")
    return record
