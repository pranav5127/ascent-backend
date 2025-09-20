import uuid
from sqlalchemy import  Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import  UUID
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"),nullable=False)
    month = Column(String, nullable=False)
    days_present = Column(Integer, default=0)
    days_absent = Column(Integer, default=0)

    student = relationship("Student", back_populates="attendance_records")
