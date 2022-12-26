from app.db.base import database
from app.pydantic.user import User, UserCreate


async def crud_get_users():
    query = "SELECT * FROM users;"
    return await database.fetch_all(query=query)


async def crud_get_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id;"
    return await database.fetch_one(query=query, values={"user_id": user_id})


async def crud_create_user(user: UserCreate):
    query = "INSERT INTO users (hashed_password, email, is_active) VALUES (:hashed_password, :email, :is_active);"
    await database.execute(query=query, values=user.dict())
    return await crud_get_user_by_email(user.email)


async def crud_get_user_by_email(email: str):
    query = "SELECT * FROM users WHERE email = :email;"
    return await database.fetch_one(query=query, values={"email": email})
