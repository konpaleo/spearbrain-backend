from fastapi import APIRouter

from app.api.routes import (
    bands,
)

api_router = APIRouter()
# api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(bands.router, prefix="/bands", tags=["Bands"])
