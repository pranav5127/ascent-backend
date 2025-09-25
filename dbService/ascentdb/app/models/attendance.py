import uuid
from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    date = Column(Date)
    status = Column(String)  # present, absent, late

    student = relationship("Profile", back_populates="attendance_records")
    cls = relationship("Class", back_populates="attendance_records")


class AttendanceMonthly(Base):
    __tablename__ = "attendance_monthly"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    month = Column(String)
    present_days = Column(Integer)
    absent_days = Column(Integer)
    late_days = Column(Integer)

    student = relationship("Profile", back_populates="attendance_monthly")
    cls = relationship("Class", back_populates="attendance_monthly")
