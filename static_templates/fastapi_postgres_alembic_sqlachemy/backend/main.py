from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.base import database
from app.core.settings import BACKEND_CORS_ORIGINS
from app.routers import router

app = FastAPI()

app.include_router(router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    await database.connect()


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()


@app.get("/")
async def read_root():
    desc = "Backend template for FastAPI, PostgreSQL, Alembic," \
           " SQLAlchemy, Pydantic, databases with asyncpg, Docker and Docker Compose."
    return {"message": desc}
