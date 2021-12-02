from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from services import customer_service
from schemas import CustomerCreate, Customer, CustomerUpdate

router = APIRouter(tags=["Customer"])


@router.post("/add_customer")
def create_customer(customer_in: CustomerCreate, db: Session = Depends(get_db)) -> Any:
    if customer_service.get_by_phone(customer_in.phone, db):
        raise HTTPException(500, detail=f"{customer_in.phone} already been added")
    if customer_service.get_by_email(customer_in.email, db):
        raise HTTPException(500, detail=f"{customer_in.email} already in use by different customer")    
    customer = customer_service.create(customer_in, db)
    if not customer:
        raise HTTPException(404, detail="Unable to add customer")
    return customer


@router.get("/customers")
def get_all_customers(db: Session = Depends(get_db)) -> Any:
    customers = customer_service.get_many(db)
    if not customers:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No customers found")
    return customers


@router.get("/customer/{id}", response_model=Customer)
def get_a_customer(id: int, db: Session = Depends(get_db)) -> Any:
    customer = customer_service.get_one(id, db)
    if not customer:
        raise HTTPException(404, detail=f"No customer for id {id}")
    return customer

