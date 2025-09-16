import uvicorn
from fastapi import FastAPI

from src.router import router
from src.config.base_configs import application_config

app = FastAPI(
    title=application_config.chat_application.rest_api.title,
    description=application_config.chat_application.rest_api.description,
    docs_url=application_config.chat_application.rest_api.docs_url,
    redoc_url=application_config.chat_application.rest_api.redoc_url,
    version=application_config.chat_application.rest_api.version
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=application_config.chat_application.rest_api.uvicorn.host,
        port=application_config.chat_application.rest_api.uvicorn.port,
        reload=application_config.chat_application.rest_api.uvicorn.reload,
    )