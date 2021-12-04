from sqlalchemy import Column, Integer, ForeignKey, Float, Text, Date, DateTime
from sqlalchemy.orm import relationship

from db.config import Base


class Bills(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_amount = Column(Float, default=0.0)
    paid_amount = Column(Float, default=0.0)
    due_amount = Column(Float, default=0.0)
    note = Column(Text)
    billing_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    bill_lines = relationship("BillLines", back_populates="bill")


class BillLines(Base):
    __tablename__ = "bill_lines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    qty = Column(Integer, default=0, nullable=False)
    profit_per_bill = Column(Float, nullable=False)

    medicine_id = Column(Integer, ForeignKey("medicines.id"))
    bill_id = Column(Integer, ForeignKey("bills.id"))

    bill = relationship("Bills", back_populates="bill_lines")
    medicine = relationship("Medicines", uselist=False, back_populates="bill_lines")
