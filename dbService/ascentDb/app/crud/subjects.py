from sqlalchemy.orm import Session
from ascentDb.app.models.subjects import Subject
from ascentDb.app.schemas.subjects import SubjectCreate

def create_subject(db: Session, sub: SubjectCreate):
    db_obj = Subject(**sub.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_subject(db: Session, subject_id):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def get_all_subjects(db: Session):
    return db.query(Subject).all()

def update_subject(db: Session, subject_id, update_data: dict):
    db_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_subject(db: Session, subject_id):
    db_obj = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
