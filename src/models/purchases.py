from sqlalchemy import Column, Integer, ForeignKey, Float, Text, Date, DateTime
from sqlalchemy.orm import relationship

from db.config import Base


class Purchases(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_amount = Column(Float, default=0.0)
    paid_amount = Column(Float, default=0.0)
    due_amount = Column(Float, default=0.0)
    note = Column(Text)
    purchase_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    purchase_lines = relationship("PurchaseLines", back_populates="purchase")


class PurchaseLines(Base):
    __tablename__ = "purchase_lines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_price = Column(Float, nullable=False)
    purchased_qty = Column(Integer, default=0)
    received_qty = Column(Integer, default=0)
    sold_qty = Column(Integer, default=0)

    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    purchase_id = Column(Integer, ForeignKey("purchases.id"))

    medicine = relationship("Medicines", uselist=False, back_populates="purchase_lines")
    purchase = relationship("Purchases", back_populates="purchase_lines")
