from sqlalchemy.orm import Session

from ascentDb.app.models import Report
from ascentDb.app.schemas.reports import ReportBase


def create_report(db: Session, report: ReportBase):
    db_obj = Report(**report.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_report(db: Session, report_id):
    return db.query(Report).filter(Report.id == report_id).first()

def get_reports_by_student(db: Session, student_id):
    return db.query(Report).filter(Report.student_id == student_id).all()

def update_report(db: Session, report_id, update_data: dict):
    db_obj = db.query(Report).filter(Report.id == report_id).first()
    if not db_obj:
        return None
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_report(db: Session, report_id):
    db_obj = db.query(Report).filter(Report.id == report_id).first()
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
