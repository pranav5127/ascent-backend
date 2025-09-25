import uuid
from sqlalchemy import Column, String, Text, Date, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    title = Column(String)
    type = Column(String)  # note, assignment, homework
    description = Column(Text)
    file_url = Column(String)
    due_date = Column(Date)
    created_at = Column(TIMESTAMP)

    cls = relationship("Class", back_populates="resources")
