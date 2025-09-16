from fastapi import APIRouter

from src.config.base_configs import application_config
from src.router import ping, chat

router = APIRouter(prefix=application_config.server.path)
router.include_router(ping.router, tags=["ping"])
router.include_router(chat.router, tags=["chat"])
