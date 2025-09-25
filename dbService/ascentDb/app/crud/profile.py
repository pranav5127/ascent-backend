from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from ascentDb.app.models.profile import Profile, UserRole
from ascentDb.app.schemas.profile import UserCreate
from ascentDb.app.security import hash_password

def create_user(db: Session, user: UserCreate):
    try:
        db_user = Profile(
            name=user.name,
            email=user.email,
            hashed_password=hash_password(user.password),
            role=user.role,
            language_pref=user.language_pref,
            mobile_number=user.mobile_number,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except StatementError as e:
        raise ValueError("Role must be 'student' or 'teacher'") from e
    return db_user

def get_user(db: Session, user_id):
    return db.query(Profile).filter(Profile.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(Profile).filter(Profile.email == email).first()

def get_all_users(db: Session):
    return db.query(Profile).all()

def update_user(db: Session, user_id, user_update: dict):
    db_user = db.query(Profile).filter(Profile.id == user_id).first()
    if not db_user:
        return None
    for key, value in user_update.items():
        if key == "password":
            setattr(db_user, "hashed_password", hash_password(value))
        elif key == "role":
            if value not in (UserRole.STUDENT.value, UserRole.TEACHER.value):
                raise ValueError("Role must be 'student' or 'teacher'")
            setattr(db_user, key, value)
        else:
            setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id):
    db_user = db.query(Profile).filter(Profile.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
