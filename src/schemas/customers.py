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
    a_positive = "A+"
    a_negative = "A-"
    b_positive = "B+"
    b_negative = "B-"
    o_positive = "O+"
    o_negative = "O-"
    ab_positive = "AB+"
    ab_negative = "AB-"


class CustomerCreate(BaseModel):
    name: str 
    email: Optional[EmailStr] = None
    phone: str
    gender: GenderEnum
    blood_group: Optional[BloodGroupEnum] = None
    birthdate: Optional[date] = None
    location: str
    country: Optional[str] = None
    zip_code: Optional[int] = None

    class Config:
        use_enum_values = True


class CustomerUpdate(CustomerCreate):
    pass


class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True


