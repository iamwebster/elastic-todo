from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str 
    surname: str | None = None
    age: int | None = Field(ge=10, le=100, default=None)
    email: EmailStr | None = None
    phone: str = Field(max_length=10)

class UserResponse(UserBase):
    id: str
    created_at: datetime 
    