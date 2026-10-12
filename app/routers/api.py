from starlette.responses import JSONResponse
from pydantic import BaseModel

from app.utils.databaze import *
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    gender: str
    age: int

@router.get("/")
def get_users():
    return BD_get_all_users()

@router.get("/{user_id}")
def get_user(user_id: int):
    user = BD_get_user_by_id(user_id)
    if not user:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return user

@router.post("/")
def create_user(data: UserCreate):
    return BD_create_user_table(
        first_name=data.first_name,
        last_name=data.last_name,
        gender=data.gender,
        age=data.age
    )
