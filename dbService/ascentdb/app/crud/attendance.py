from sqlalchemy.orm import Session

from ascentdb.app.models import AttendanceRecord, AttendanceMonthly
from ascentdb.app.schemas.attendance import AttendanceRecordBase, AttendanceMonthlyBase


def add_attendance(db: Session, record: AttendanceRecordBase):
    db_obj = AttendanceRecord(**record.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_attendance(db: Session, record_id):
    return db.query(AttendanceRecord).filter(AttendanceRecord.id == record_id).first()

def get_attendance_by_class(db: Session, class_id, date=None):
    query = db.query(AttendanceRecord).filter(AttendanceRecord.class_id == class_id)
    if date:
        query = query.filter(AttendanceRecord.date == date)
    return query.all()

# Monthly
def add_attendance_monthly(db: Session, record: AttendanceMonthlyBase):
    db_obj = AttendanceMonthly(**record.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_attendance_monthly(db: Session, student_id, month):
    return db.query(AttendanceMonthly).filter(
        AttendanceMonthly.student_id == student_id,
        AttendanceMonthly.month == month
    ).first()
