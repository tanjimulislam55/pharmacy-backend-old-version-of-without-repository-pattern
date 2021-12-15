from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List, Optional
    

class BillLineCreate(BaseModel):
    price: float
    qty: int = Field(..., gt=0, description="The quantity must be greater than zero")
    medicine_id: int


class BillLine(BillLineCreate):
    id: int
    bill_id: int

    class Config: 
        orm_mode = True


class BillCreate(BaseModel):
    total_amount: Optional[float]
    due_amount: Optional[float]
    paid_amount: Optional[float]
    note: Optional[str] = None
    billing_date: date = date.today()
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class Bill(BillCreate):
    id: int
    bill_lines: Optional[List[BillLine]] = None

    class Config: 
        orm_mode = True