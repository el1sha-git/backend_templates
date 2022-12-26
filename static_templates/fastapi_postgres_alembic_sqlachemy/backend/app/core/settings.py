from os import getenv

# Get postgresql credentials from environment variables
POSTGRES_USER = getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "admin")
POSTGRES_HOST = getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = getenv("POSTGRES_DB", "postgres")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Add cors origins
BACKEND_CORS_ORIGINS = [
    "http://localhost:8080"
]
