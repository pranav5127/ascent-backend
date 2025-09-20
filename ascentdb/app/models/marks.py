import uuid
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import  UUID, JSONB
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class Marks(Base):
    __tablename__ = "marks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    exam_type = Column(String, nullable=False)
    subject_scores = Column(JSONB, nullable=False)
    date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="marks_records")