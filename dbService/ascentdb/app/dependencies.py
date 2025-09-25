from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from ascentdb.app.database import get_db
from ascentdb.app.models.profile import Profile, UserRole
from ascentdb.app.security import decode_token

def get_current_user(token: str = Depends(...), db: Session = Depends(get_db)) -> Profile:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(Profile).filter(Profile.id == user_id).first()
    if not user:
        raise credentials_exception
    return user

def require_role(role: UserRole):
    def role_checker(current_user: Profile = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return current_user
    return role_checker
