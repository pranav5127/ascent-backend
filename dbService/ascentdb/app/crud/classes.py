from sqlalchemy.orm import Session

from ascentdb.app.models import Class, ClassStudent
from ascentdb.app.schemas.class_schemas import ClassCreate, ClassStudentCreate


def create_class(db: Session, cls: ClassCreate):
    db_obj = Class(**cls.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_class(db: Session, class_id):
    return db.query(Class).filter(Class.id == class_id).first()

def get_all_classes(db: Session):
    return db.query(Class).all()

def update_class(db: Session, class_id, update_data: dict):
    db_obj = db.query(Class).filter(Class.id == class_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_class(db: Session, class_id):
    db_obj = db.query(Class).filter(Class.id == class_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj

# ClassStudent CRUD
def add_student_to_class(db: Session, student: ClassStudentCreate):
    db_obj = ClassStudent(**student.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_students_in_class(db: Session, class_id):
    return db.query(ClassStudent).filter(ClassStudent.class_id == class_id).all()


def remove_student_from_class(db: Session, student_id, class_id):
    db_obj = db.query(ClassStudent).filter(
        ClassStudent.student_id == student_id, ClassStudent.class_id == class_id
    ).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
