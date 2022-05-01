import logging

from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

logger = logging.getLogger('shared.logging.logger')


async def exception_callback(request: Request, exc: Exception):
    logger.exception(exc)
    return JSONResponse({"detail": "Internal server error"}, status_code=HTTP_500_INTERNAL_SERVER_ERROR)
