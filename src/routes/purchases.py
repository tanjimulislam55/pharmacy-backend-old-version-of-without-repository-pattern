from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from services import purchase_service
from schemas import PurchaseCreate, Purchase, PurchaseLine, PurchaseLineCreate, purchases

router = APIRouter(tags=["Purchase"])


@router.post("/add_purchase", response_model=Purchase)
def create_purchase(purchase_in: PurchaseCreate, purchase_line_in: List[PurchaseLineCreate], db: Session = Depends(get_db)) -> Any:
    try:
        purchase = purchase_service.create(purchase_in, purchase_line_in, db)
        return purchase
    except:
        raise HTTPException(404, detail="Unable to add purchase")


@router.get("/purchases", response_model=List[Purchase])
def get_all_purchases(db: Session = Depends(get_db)) -> Any:
    purchases = purchase_service.get_many(db)
    if not purchases:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No purchases found")
    return purchases


@router.get("/purchase/{id}", response_model=Purchase)
def get_all_purchases(di: int, db: Session = Depends(get_db)) -> Any:
    purchase = purchase_service.get_one(id, db)
    if not purchase:
        raise HTTPException(404, detail=f"No purchase for id {id}")
    return purchase