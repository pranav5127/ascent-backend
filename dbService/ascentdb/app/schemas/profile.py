from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from uuid import UUID
from enum import Enum

class UserRole(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    language_pref: Optional[str] = None
    mobile_number: Optional[str] = None

    @validator("role")
    def role_must_be_student_or_teacher(cls, v):
        if v not in (UserRole.STUDENT.value, UserRole.TEACHER.value):
            raise ValueError("Role must be 'student' or 'teacher'")
        return v

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: UUID

    model_config = {
         "from_attributes": True
        }
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[str] = None
    role: Optional[str] = None
