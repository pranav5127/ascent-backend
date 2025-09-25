from sqlalchemy.orm import Session

from ascentdb.app.models import Resource
from ascentdb.app.schemas.resources import ResourceBase


def add_resource(db: Session, resource: ResourceBase):
    db_obj = Resource(**resource.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_resource(db: Session, resource_id):
    return db.query(Resource).filter(Resource.id == resource_id).first()

def get_resources_by_class_and_subject(db: Session, class_id, subject_id):
    return (
        db.query(Resource)
        .filter(Resource.class_id == class_id, Resource.subject_id == subject_id)
        .all()
    )


def update_resource(db: Session, resource_id, update_data: dict):
    db_obj = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_resource(db: Session, resource_id):
    db_obj = db.query(Resource).filter(Resource.id == resource_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
