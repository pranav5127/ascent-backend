import uuid
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentDb.app.database import Base

class ProgressTracking(Base):
    __tablename__ = "progress_tracking"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"), nullable=False)
    metric_type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    recorded_at = Column(DateTime, nullable=False)

    student = relationship("Profile", back_populates="progress_records")


class ClassProgress(Base):
    __tablename__ = "class_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"), nullable=False)
    period = Column(String, nullable=False)  # YYYY-MM
    avg_marks = Column(Float, nullable=True)
    attendance_rate = Column(Float, nullable=True)
    submission_rate = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False)

    cls = relationship("Class", back_populates="progress_records")
