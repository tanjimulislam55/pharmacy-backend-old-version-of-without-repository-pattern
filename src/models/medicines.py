from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from db.config import Base


class Units(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False, unique=True)

    medicines = relationship("Medicines", back_populates="unit_name")


class Types(Base):
    __tablename__ = "types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False, unique=True)

    medicines = relationship("Medicines", back_populates="type_name")


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False, unique=True)

    medicines = relationship("Medicines", back_populates="category_name")


class Medicines(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True, nullable=False)

    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    unit_id = Column(Integer, ForeignKey("units.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    # here should be a generic name column

    vendor = relationship("Vendors", back_populates="medicines")
    unit_name = relationship("Units", back_populates="medicines")
    type_name = relationship("Types", back_populates="medicines")
    category_name = relationship("Categories", back_populates="medicines")
    medicine_detail = relationship("MedicineDetails", uselist=False, back_populates="medicine")
    purchase_lines = relationship("PurchaseLines", back_populates="medicine")


class MedicineDetails(Base):
    __tablename__ = "medicine_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    retail_price = Column(Float, nullable=False, default=0.0)
    stock = Column(Integer, default=0)

    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    
    medicine = relationship("Medicines", back_populates="medicine_detail")


