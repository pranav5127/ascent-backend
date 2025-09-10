import  uuid
from sqlalchemy import Column, String, Date, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import  relationship
from ascentdb.app.database import Base

class Activities(Base):
    __tablename__ = "activities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4(), unique=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    activity_type = Column(String, nullable=False)
    description = Column(Text)
    achievement = Column(String)
    date = Column(Date, nullable=False)

    student = relationship("Student", back_populates="activities_records")
