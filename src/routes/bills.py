from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from services import bill_service, purchase_service
from schemas import Bill, BillCreate, BillLine, BillLineCreate

router = APIRouter(tags=["Bill"])


@router.post("/add_bill", response_model=Bill)
def create_bill(bill_in: BillCreate, bill_line_in: List[BillLineCreate], db: Session = Depends(get_db)) -> Any:
    try:
        if not purchase_service.has_available_qty(bill_line_in, db):
            raise HTTPException(500, detail=f"Not enough available medicine for sale")
        bill = bill_service.create(bill_in, bill_line_in, db)
        return bill
    except NameError:
        print(NameError)
        raise HTTPException(404, detail="Unable to add bill")


@router.get("/bills", response_model=List[Bill])
def get_all_bills(db: Session = Depends(get_db)) -> Any:
    bills = bill_service.get_many(db)
    if not bills:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No bills found")
    return bills


@router.get("/bill/{id}", response_model=Bill)
def get_a_bill(id: int, db: Session = Depends(get_db)) -> Any:
    bill = bill_service.get_one(id, db)
    if not bill:
        raise HTTPException(404, detail=f"No bill for id {id}")
    return bill