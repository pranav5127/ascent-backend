from pydantic import  BaseModel, EmailStr
from uuid import UUID
from datetime import  datetime
from ascentdb.app.core.enums import UserRole

class UserBase(BaseModel):
    email: EmailStr
    role: UserRole
    mobile_number: str

class UserCreate(UserBase):
    external_id: str

class UserUpdate(BaseModel):
    email: EmailStr | None
    role: UserRole |None

class UserResponse(UserBase):
    id: UUID
    external_id: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }