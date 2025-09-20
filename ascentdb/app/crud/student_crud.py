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
    db_student = Student(**student.model_dump())
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
    existing = db.query(Attendance).filter(
        Attendance.student_id == attendance.student_id,
        Attendance.month == attendance.month
    ).first()
    if existing:
        existing.days_present = attendance.days_present
        existing.days_absent = attendance.days_absent
        db.commit()
        db.refresh(existing)
        return existing

    db_attendance = Attendance(**attendance.model_dump())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance


def get_attendance_by_student(db: Session, student_id):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()

# ---------------- Marks ----------------
def create_marks(db: Session, marks: MarksCreate):
    existing = db.query(Marks).filter(
        Marks.student_id == marks.student_id,
        Marks.exam_type == marks.exam_type
    ).first()
    if existing:
        existing.subject_scores = marks.subject_scores
        existing.date = marks.date
        db.commit()
        db.refresh(existing)
        return existing

    db_marks = Marks(**marks.model_dump())
    db.add(db_marks)
    db.commit()
    db.refresh(db_marks)
    return db_marks


def get_marks_by_student(db: Session, student_id):
    return db.query(Marks).filter(Marks.student_id == student_id).all()

# ---------------- Activities ----------------
def create_activity(db: Session, activity: ActivitiesCreate):
    existing_activity = None
    if getattr(activity, "id", None):
        existing_activity = db.query(Activities).filter(Activities.id == activity.id).first()
    else:
        existing_activity = (
            db.query(Activities)
            .filter(
                Activities.student_id == activity.student_id,
                Activities.activity_type == activity.activity_type,
                Activities.date == activity.date
            )
            .first()
        )

    if existing_activity:
        # Update existing record
        existing_activity.activity_type = activity.activity_type
        existing_activity.description = activity.description
        existing_activity.achievement = activity.achievement
        existing_activity.date = activity.date
        db.commit()
        db.refresh(existing_activity)
        return existing_activity

    db_activity = Activities(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activities_by_student(db: Session, student_id):
    return db.query(Activities).filter(Activities.student_id == student_id).all()


# ---------------- Reports ----------------
def create_or_update_report(db: Session, report: ReportsCreate):
    existing_report = db.query(Reports).filter(Reports.student_id == report.student_id).first()
    if existing_report:
        existing_report.report = report.report
        existing_report.summary = report.summary
        db.commit()
        db.refresh(existing_report)

        existing_report.student_name = existing_report.student.name if existing_report.student else None
        existing_report.parent_mobile = (
            existing_report.student.parent.mobile_number
            if existing_report.student and existing_report.student.parent else None
        )
        return existing_report

    db_report = Reports(**report.model_dump())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    db_report.student_name = db_report.student.name if db_report.student else None
    db_report.parent_mobile = (
        db_report.student.parent.mobile_number
        if db_report.student and db_report.student.parent else None
    )
    return db_report


def get_reports_by_student(db: Session, student_id: str):
    report = db.query(Reports).filter(Reports.student_id == student_id).first()
    if not report:
        return None

    report.student_name = report.student.name if report.student else None
    report.parent_mobile = (
        report.student.parent.mobile_number if report.student and report.student.parent else None
    )
    return report


