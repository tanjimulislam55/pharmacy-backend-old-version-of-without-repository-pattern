from sqlalchemy import Column, Integer, String, Enum, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from db.config import Base

class GenderEnum(str, enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class BloodGroupEnum(str, enum.Enum):
    ap = "A+"
    an = "A-"
    bp = "B+"
    bn = "B-"
    op = "O+"
    on = "O-"
    abp = "AB+"
    abn = "AB-"


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(14), unique=True)
    gender = Column(Enum(GenderEnum), nullable=False)
    bloodgroup = Column(Enum(BloodGroupEnum))
    city = Column(String(20))
    birthdate = Column(Date)
    location = Column(String(255), nullable=False)
    country = Column(String(30))
    zip_code = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
