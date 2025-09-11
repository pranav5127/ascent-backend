from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4, UUID

from ascentdb.app.database import get_db
from ascentdb.app.models.user import User
from ascentdb.app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

# Create a new user (parent or teacher)
@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email or external_id already exists
    existing_user = db.query(User).filter(
        (User.email == user.email) | (User.external_id == user.external_id)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email or external_id already exists")

    new_user = User(
        id=uuid4(),
        email=user.email,
        external_id=user.external_id,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# List all users
@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Get a user by ID
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user





