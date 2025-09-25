import uuid
from sqlalchemy import Column, String, Text, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ascentdb.app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    recipient_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"))
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    type = Column(String)
    message = Column(Text)
    created_at = Column(TIMESTAMP)
    read = Column(Boolean, default=False)

    recipient = relationship("Profile", back_populates="notifications")
    cls = relationship("Class", back_populates="notifications")
