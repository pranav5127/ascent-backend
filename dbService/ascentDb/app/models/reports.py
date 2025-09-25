import uuid
from sqlalchemy import Column, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentDb.app.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    period = Column(String)
    report_text = Column(Text)
    created_at = Column(TIMESTAMP)

    student = relationship("Profile", back_populates="reports")
    cls = relationship("Class", back_populates="reports")
