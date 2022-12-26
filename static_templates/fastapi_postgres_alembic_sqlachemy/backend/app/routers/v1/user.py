from fastapi import APIRouter

from app.db.crud.user import crud_get_users, crud_get_user, crud_create_user, crud_get_user_by_email
from app.pydantic.user import User, UserCreate

user_router = APIRouter()


@user_router.get("/all", response_model=list[User])
async def get_users():
    return await crud_get_users()


@user_router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return await crud_get_user(user_id)


@user_router.post("/", response_model=User)
async def create_user(user: UserCreate):
    await crud_create_user(user)
    return await crud_get_user_by_email(user.email)

