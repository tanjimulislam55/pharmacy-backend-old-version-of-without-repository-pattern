from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import relationship
import enum

from db.config import Base

class GenderEnum(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class BloodGroupEnum(enum.Enum):
    a_positive = "A+"
    a_negative = "A-"
    b_positive = "B+"
    b_negative = "B-"
    o_positive = "O+"
    o_negative = "O-"
    ab_positive = "AB+"
    ab_negative = "AB-"


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(14), unique=True)
    gender = Column(Enum(GenderEnum), nullable=False)
    blood_group = Column(Enum(BloodGroupEnum))
    city = Column(String(20))
    birthdate = Column(Date)
    location = Column(String(255), nullable=False)
    country = Column(String(30))
    zip_code = Column(Integer)
    
