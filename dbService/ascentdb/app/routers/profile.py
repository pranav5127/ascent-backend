from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from ascentdb.app.crud.profile import create_user, get_user, get_all_users, update_user, delete_user
from ascentdb.app.database import get_db
from ascentdb.app.schemas.profile import UserResponse, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return db_user

@router.get("/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id: UUID, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[UserResponse])
def get_all_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: UUID, user_update: dict, db: Session = Depends(get_db)):
    try:
        db_user = update_user(db, user_id, user_update)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=UserResponse)
def delete_user_endpoint(user_id: UUID, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
