from fastapi import APIRouter
from .router import chat, ping
from config import settings

api_router = APIRouter(prefix=settings.server.path)
api_router.include_router(chat.router, tags=["chat"])
api_router.include_router(ping.router, tags=["ping"])
