from fastapi import APIRouter
from starlette.responses import JSONResponse

from domain.req.chat import UserQueryRequest

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("")
def openai_function_calling_auth(user_query_request: UserQueryRequest) -> JSONResponse:
    original = user_query_request.query
    return {
        "original": original,
        "new": "ping"
    }
