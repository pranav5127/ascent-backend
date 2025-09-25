import uuid
from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    name = Column(String, nullable=False)
    date = Column(Date)

    cls = relationship("Class", back_populates="exams")
    marks = relationship("ExamMark", back_populates="exam")


class ExamMark(Base):
    __tablename__ = "exam_marks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_id = Column(UUID(as_uuid=True), ForeignKey("exams.id"))
    student_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))
    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"))
    marks = Column(Integer)

    exam = relationship("Exam", back_populates="marks")
    student = relationship("Profile", back_populates="exam_marks")
