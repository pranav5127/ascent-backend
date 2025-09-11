# app/crud/crud.py
from sqlalchemy.orm import Session
from ascentdb.app.models.student import Student
from ascentdb.app.models.attendance import Attendance
from ascentdb.app.models.marks import Marks
from ascentdb.app.models.activities import Activities
from ascentdb.app.models.reports import Reports
from ascentdb.app.schemas.student import StudentCreate
from ascentdb.app.schemas.attendance import AttendanceCreate
from ascentdb.app.schemas.marks import MarksCreate
from ascentdb.app.schemas.activities import ActivitiesCreate
from ascentdb.app.schemas.reports import ReportsCreate

# ---------------- Student ----------------
def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student(db: Session, student_id):
    return db.query(Student).filter(Student.id == student_id).first()

# ---------------- Attendance ----------------
def create_attendance(db: Session, attendance: AttendanceCreate):
    db_attendance = Attendance(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_attendance_by_student(db: Session, student_id):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()

# ---------------- Marks ----------------
def create_marks(db: Session, marks: MarksCreate):
    db_marks = Marks(**marks.dict())
    db.add(db_marks)
    db.commit()
    db.refresh(db_marks)
    return db_marks

def get_marks_by_student(db: Session, student_id):
    return db.query(Marks).filter(Marks.student_id == student_id).all()

# ---------------- Activities ----------------
def create_activity(db: Session, activity: ActivitiesCreate):
    db_activity = Activities(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activities_by_student(db: Session, student_id):
    return db.query(Activities).filter(Activities.student_id == student_id).all()

# ---------------- Reports ----------------
def create_report(db: Session, report: ReportsCreate):
    db_report = Reports(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_reports_by_student(db: Session, student_id):
    return db.query(Reports).filter(Reports.student_id == student_id).all()
