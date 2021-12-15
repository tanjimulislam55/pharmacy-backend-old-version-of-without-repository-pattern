from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from enum import Enum
from datetime import date


class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class BloodGroupEnum(str, Enum):
    ap = "A+"
    an = "A-"
    bp = "B+"
    bn = "B-"
    op = "O+"
    on = "O-"
    abp = "AB+"
    abn = "AB-"


class CustomerCreate(BaseModel):
    name: str 
    email: Optional[EmailStr] = None
    phone: str
    gender: GenderEnum
    bloodgroup: Optional[BloodGroupEnum] = None
    birthdate: Optional[date] = None
    location: str
    city: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[int] = None

    class Config:
        use_enum_values = True


class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True


class CustomerUpdate(CustomerCreate):
    name: Optional[str] 
    email: Optional[EmailStr] = None
    phone: Optional[str]
    gender: Optional[GenderEnum]
    bloodgroup: Optional[BloodGroupEnum] = None
    birthdate: Optional[date] = None
    location: Optional[str]
    city: Optional[str] = None
    country: Optional[str] = None
    zip_code: Optional[int] = None

    class Config:
        use_enum_values = True

