import uuid
from sqlalchemy import  Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import  func
from dbService.ascentdb.app.database import Base

class Reports(Base):
    __tablename__  = "reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    report = Column(JSONB, nullable=False)
    summary = Column(JSONB, nullable=False)
    generated_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("Student", back_populates="reports")