from fastapi import APIRouter
from app.routers.v1.user import user_router

router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["user"])
