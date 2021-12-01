from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from schemas.medicines import MedicineDetailUpdate
from services import medicine_service, type_service, category_service, unit_service
from schemas import MedicineDetail, Medicine, MedicineDetailCreate, MedicineCreate, TypeCreate, Type, UnitCreate, Unit, Category, CategoryCreate


router = APIRouter(tags=["Medicine"])


@router.post("/add_medicine", response_model=Medicine)
def create_medicine(medicine_in: MedicineCreate, db: Session = Depends(get_db)) -> Any:
    if medicine_service.get_by_name(medicine_in.name, db):
        raise HTTPException(500, detail=f"{medicine_in.name} already been added")
    medicine = medicine_service.create(medicine_in, db)
    if not medicine:
        raise HTTPException(404, detail="Unable to add medicine")
    return medicine


@router.get("/medicines", response_model=List[Medicine])
def get_all_medicines(db: Session = Depends(get_db)) -> Any:
    medicines = medicine_service.get_many(db)
    if not medicines:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No medicine found")
    return medicines


@router.get("/medicine/{id}", response_model=Medicine)
def get_a_medicine(id: int, db: Session = Depends(get_db)) -> Any:
    medicine = medicine_service.get_one(id, db)
    if not medicine:
        raise HTTPException(404, detail=f"No medicine for id {id}")
    return medicine


@router.put("/medicine/{id}", response_model=Medicine)
def update_a_medicine(id: int, db_in: MedicineDetailUpdate, db: Session = Depends(get_db)) -> Any:
    if medicine_service.get_one(id, db):
        medicine = medicine_service.update(id, db_in)
        if not medicine:
            JSONResponse(status_code=status.HTTP_304_NOT_MODIFIED, content="Could not update medicine detail")
    raise HTTPException(404, detail=f"No medicine for id {id}")


@router.post("/add_type", response_model=Type)
def create_type(type_in: TypeCreate, db: Session = Depends(get_db)) -> Any:
    if type_service.get_by_name(type_in.name, db):
        raise HTTPException(500, detail=f"{type_in.name} already been added")
    medicine_type = type_service.create(type_in, db)
    if not medicine_type:
        raise HTTPException(404, detail="Unable to add medicine type")
    return medicine_type


@router.post("/add_category", response_model=Category)
def create_type(category_in: CategoryCreate, db: Session = Depends(get_db)) -> Any:
    if category_service.get_by_name(category_in.name, db):
        raise HTTPException(500, detail=f"{category_in.name} already been added")
    medicine_category = category_service.create(category_in, db)
    if not medicine_category:
        raise HTTPException(404, detail="Unable to add medicine category")
    return medicine_category


@router.post("/add_unit", response_model=Unit)
def create_type(unit_n: UnitCreate, db: Session = Depends(get_db)) -> Any:
    if unit_service.get_by_name(unit_n.name, db):
        raise HTTPException(500, detail=f"{unit_n.name} already been added")
    medicine_unit = unit_service.create(unit_n, db)
    if not medicine_unit:
        raise HTTPException(404, detail="Unable to add medicine unit")
    return medicine_unit


@router.get("/types", response_model=List[Type])
def get_all_types(db: Session = Depends(get_db)) -> Any:
    types = type_service.get_many(db)
    if not types:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No types found")
    return types


@router.get("/units", response_model=List[Type])
def get_all_types(db: Session = Depends(get_db)) -> Any:
    units = unit_service.get_many(db)
    if not units:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No units found")
    return units


@router.get("/categories", response_model=List[Type])
def get_all_types(db: Session = Depends(get_db)) -> Any:
    categories = category_service.get_many(db)
    if not categories:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No categories found")
    return categories


