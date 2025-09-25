from sqlalchemy.orm import Session
from uuid import UUID

from ascentDb.app.models import ProgressTracking, ClassProgress
from ascentDb.app.schemas.progress import ProgressTrackingBase, ClassProgressBase

# CRUD for ProgressTracking
def add_progress(db: Session, progress: ProgressTrackingBase):
    db_obj = ProgressTracking(**progress.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_progress(db: Session, progress_id: UUID):
    return db.query(ProgressTracking).filter(ProgressTracking.id == progress_id).first()

def get_all_progress(db: Session):
    return db.query(ProgressTracking).all()

def update_progress(db: Session, progress_id: UUID, update_data: dict):
    db_obj = db.query(ProgressTracking).filter(ProgressTracking.id == progress_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_progress(db: Session, progress_id: UUID):
    db_obj = db.query(ProgressTracking).filter(ProgressTracking.id == progress_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj

# CRUD for ClassProgress
def add_class_progress(db: Session, progress: ClassProgressBase):
    db_obj = ClassProgress(**progress.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_class_progress(db: Session, class_id: UUID, period: str):
    return db.query(ClassProgress).filter(
        ClassProgress.class_id == class_id,
        ClassProgress.period == period
    ).first()

def get_all_class_progress(db: Session):
    return db.query(ClassProgress).all()

def update_class_progress(db: Session, progress_id: UUID, update_data: dict):
    db_obj = db.query(ClassProgress).filter(ClassProgress.id == progress_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_class_progress(db: Session, progress_id: UUID):
    db_obj = db.query(ClassProgress).filter(ClassProgress.id == progress_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
