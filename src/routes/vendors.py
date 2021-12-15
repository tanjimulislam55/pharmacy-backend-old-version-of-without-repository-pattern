from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from services import vendor_service
from schemas import VendorCreate, Vendor, VendorUpdate

router = APIRouter(tags=["Vendor"])


@router.post("/add_vendor", response_model=Vendor)
def create_vendor(vendor_in: VendorCreate, db: Session = Depends(get_db)) -> Any:
    if vendor_service.get_by_name(vendor_in.name, db):
        raise HTTPException(500, detail=f"{vendor_in.name} already been added")
    if vendor_service.get_by_mobile(vendor_in.mobile, db):
        raise HTTPException(500, detail=f"{vendor_in.mobile} already in use by different vendor")
    vendor = vendor_service.create(vendor_in, db)
    if not vendor:
        raise HTTPException(404, detail="Unable to add vendor")
    return vendor


@router.get("/vendors", response_model=List[Vendor])
def get_all_vendors(db: Session = Depends(get_db)) -> Any:
    vendors = vendor_service.get_many(db)
    if not vendors:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No vendors found")
    return vendors


@router.get("/vendor/{id}", response_model=Vendor)
def get_a_vendor(id: int, db: Session = Depends(get_db)) -> Any:
    vendor = vendor_service.get_one(id, db)
    if not vendor:
        raise HTTPException(404, detail=f"No vendor for id {id}")
    return vendor


@router.put("/vendor/{id}", response_model=Vendor)
def update_a_vendor(id: int, vendor_in: VendorUpdate, db: Session = Depends(get_db)) -> Any:
    try:
        updated_vendor = vendor_service.update(id, vendor_in, db)
        if not updated_vendor:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Could not update vendor")
        return updated_vendor
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This vendor cannot be deleted as it is associated with medicine/s`")