import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentDb.app.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))

    # Relationships
    teacher = relationship("Profile", back_populates="classes_taught")
    students = relationship("ClassStudent", back_populates="cls")
    progress_records = relationship("ClassProgress", back_populates="cls")
    attendance_records = relationship("AttendanceRecord", back_populates="cls")
    attendance_monthly = relationship("AttendanceMonthly", back_populates="cls")
    exams = relationship("Exam", back_populates="cls")
    reports = relationship("Report", back_populates="cls")
    resources = relationship("Resource", back_populates="cls")
    subjects = relationship("Subject", back_populates="cls")
    notifications = relationship("Notification", back_populates="cls")


class ClassStudent(Base):
    __tablename__ = "class_students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))

    # Relationships
    cls = relationship("Class", back_populates="students")
    student = relationship("Profile", back_populates="enrolled_classes")
