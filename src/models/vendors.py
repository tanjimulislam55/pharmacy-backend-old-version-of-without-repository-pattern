from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.config import Base


class Vendors(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    mobile = Column(String(20), unique=True)

    medicines = relationship("Medicines", back_populates="vendor") 