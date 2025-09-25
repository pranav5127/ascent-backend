import uuid
from enum import Enum
from sqlalchemy import Column, String, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentDb.app.database import Base

class UserRole(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole, name="user_role"), nullable=False)
    language_pref = Column(String)
    mobile_number = Column(String, unique=True, nullable=True)

    # Relationships
    classes_taught = relationship("Class", back_populates="teacher")
    enrolled_classes = relationship("ClassStudent", back_populates="student")
    progress_records = relationship("ProgressTracking", back_populates="student")
    attendance_records = relationship("AttendanceRecord", back_populates="student")
    attendance_monthly = relationship("AttendanceMonthly", back_populates="student")
    exam_marks = relationship("ExamMark", back_populates="student")
    reports = relationship("Report", back_populates="student")
    notifications = relationship("Notification", back_populates="recipient")
