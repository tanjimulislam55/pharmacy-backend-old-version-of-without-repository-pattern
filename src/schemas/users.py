from typing import Optional
from pydantic import BaseModel, EmailStr


class RoleCreate(BaseModel):
    rolename: str


class RoleUpdate(RoleCreate):
    pass


class Role(RoleCreate):
    id: int

    class Config:
        orm_mode = True

        
class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class User(UserBase):
    id: int

    class Config:
        orm_mode = True