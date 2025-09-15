import uvicorn
from fastapi import FastAPI

from api import api_router
from config import settings

app = FastAPI(
    title="Demo API",
    description="Demo API",
    docs_url="/docs",
    redoc_url="/redoc",
    version="1.0.0")

app.include_router(api_router)

# run debug
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.server.port
    )
