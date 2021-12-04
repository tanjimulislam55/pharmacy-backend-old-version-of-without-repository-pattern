from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional
    

class PurchaseLineCreate(BaseModel):
    purchase_price: float
    purchased_qty: int
    received_qty: Optional[int] = 0
    sold_qty: Optional[int] = 0
    medicine_id: int

    class Config:
        schema_extra = {
            "example": {
                "purchase_price": 0.0,
                "purchased_qty": 0,
                "medicine_id": 0,
                "received_qty": 0
            }
        }


class PurchaseLine(PurchaseLineCreate):
    id: int 

    class Config: 
        orm_mode = True


class PurchaseCreate(BaseModel):
    total_amount: Optional[float]
    due_amount: Optional[float]
    paid_amount: Optional[float]
    note: Optional[str] = None
    purchase_date: date = date.today()
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class Purchase(PurchaseCreate):
    id: int
    purchase_lines: Optional[List[PurchaseLine]] = None

    class Config: 
        orm_mode = True