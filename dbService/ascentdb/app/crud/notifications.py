from sqlalchemy.orm import Session

from ascentdb.app.models import Notification
from ascentdb.app.schemas.notifications import NotificationBase


def create_notification(db: Session, note: NotificationBase):
    db_obj = Notification(**note.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_notification(db: Session, note_id):
    return db.query(Notification).filter(Notification.id == note_id).first()

def get_notifications_for_user(db: Session, user_id):
    return db.query(Notification).filter(Notification.recipient_id == user_id).all()

def mark_notification_read(db: Session, note_id):
    db_obj = db.query(Notification).filter(Notification.id == note_id).first()
    if db_obj:
        db_obj.read = True
        db.commit()
        db.refresh(db_obj)
    return db_obj
