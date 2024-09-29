from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str 
    surname: str | None = None
    age: int | None = Field(ge=10, le=100)
    email: EmailStr | None = None
    phone: str = Field(max_length=10)
    created_at: datetime 
