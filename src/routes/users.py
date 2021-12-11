from typing import Any, List
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from db.config import get_db
from services import user_service, role_service
from schemas import User, RoleCreate, Role, UserCreate, UserUpdate
from utils.auth import get_current_active_user


router = APIRouter(tags=["User"])


@router.post("/add_role", response_model=Role)
def create_role(role_in: RoleCreate, db: Session = Depends(get_db)) -> Any:
    role = role_service.create(role_in, db)
    if not role:
        raise HTTPException(404, detail="Unable to add role")
    return role


@router.get("/roles", response_model=List[Role])
def get_all_roles(db: Session = Depends(get_db)) -> Any:
    roles = role_service.get_many(db)
    if not roles:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No roles found")
    return roles


@router.post("/add_user", response_model=User)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)) -> Any:
    if user_service.get_by_email(user_in.email, db):
        raise HTTPException(500, detail="Email already taken")
    if user_service.get_by_username(user_in.username, db):
        raise HTTPException(500, detail="Username already taken")
    user = user_service.create(user_in, db)
    if not user:
        raise HTTPException(404, detail="Unable to register a user")
    return user


@router.get("/get_users", response_model=List[User])
def get_all_users(db: Session = Depends(get_db)) -> Any:
    users = user_service.get_many(db)
    if not users:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No users found")
    return users


@router.get("/get_user/{id}", response_model=User)
def get_a_user(id: int, db: Session = Depends(get_db)) -> Any:
    user = user_service.get_one(id, db)
    if not user:
        raise HTTPException(404, detail=f"No user for id {id}")
    return user


@router.put("/update_user/{id}", response_model=User)
def update_a_user(id: int, user_in: UserUpdate, db: Session = Depends(get_db)) -> Any:
    user = user_service.update(id, user_in, db)
    if not user:
        raise HTTPException(404, detail="Unable to update a user")
    return user


@router.put("/update_user_role/{id}", response_model=User)
def update_user_role(id: int, role_id: int, db: Session = Depends(get_db)) -> Any:
    user = user_service.update_role(id, role_id, db)
    if not user:
        raise HTTPException(404, detail="Unable to update a user")
    return user


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
    