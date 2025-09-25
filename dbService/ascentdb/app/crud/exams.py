from sqlalchemy.orm import Session
from ascentdb.app.models import Exam, ExamMark, Subject
from ascentdb.app.schemas.exams import ExamCreate, ExamMarkBase

def create_exam(db: Session, exam: ExamCreate):
    db_obj = Exam(**exam.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_exam(db: Session, exam_id):
    return db.query(Exam).filter(Exam.id == exam_id).first()


def get_all_exams(db: Session):
    return db.query(Exam).all()


def update_exam(db: Session, exam_id, update_data: dict):
    db_obj = db.query(Exam).filter(Exam.id == exam_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_exam(db: Session, exam_id):
    db_obj = db.query(Exam).filter(Exam.id == exam_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj

def add_exam_mark(db: Session, mark: ExamMarkBase):
    exam = db.query(Exam).filter(Exam.id == mark.exam_id).first()
    if not exam:
        raise ValueError("Exam not found")

    subject = db.query(Subject).filter(
        Subject.id == mark.subject_id,
        Subject.class_id == exam.class_id
    ).first()

    if not subject:
        raise ValueError("Subject does not belong to the class of this exam")

    db_obj = ExamMark(**mark.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_exam_marks(db: Session, exam_id):
    return db.query(ExamMark).filter(ExamMark.exam_id == exam_id).all()

def get_student_marks_for_exam(db: Session, student_id, exam_id):
    return (
        db.query(ExamMark)
        .filter(ExamMark.student_id == student_id, ExamMark.exam_id == exam_id)
        .all()
    )

