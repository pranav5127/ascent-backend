from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from ascentDb.app.database import get_db
from ascentDb.app.schemas.notifications import NotificationBase, NotificationResponse
from ascentDb.app.crud.notifications import create_notification, get_notification, get_notifications_for_user, mark_notification_read

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/", response_model=NotificationResponse)
def create_notification_endpoint(notification: NotificationBase, db: Session = Depends(get_db)):
    return create_notification(db, notification)

@router.get("/{notification_id}", response_model=NotificationResponse)
def get_notification_endpoint(notification_id: UUID, db: Session = Depends(get_db)):
    note = get_notification(db, notification_id)
    if not note:
        raise HTTPException(status_code=404, detail="Notification not found")
    return note

@router.get("/user/{user_id}", response_model=List[NotificationResponse])
def get_notifications_for_user_endpoint(user_id: UUID, db: Session = Depends(get_db)):
    return get_notifications_for_user(db, user_id)

@router.put("/{notification_id}/read", response_model=NotificationResponse)
def mark_notification_read_endpoint(notification_id: UUID, db: Session = Depends(get_db)):
    note = mark_notification_read(db, notification_id)
    if not note:
        raise HTTPException(status_code=404, detail="Notification not found")
    return note
