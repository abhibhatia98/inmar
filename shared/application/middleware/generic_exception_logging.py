import logging
from starlette.requests import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from shared.logging.custom_dimension import CustomDimension
from shared.logging.logging_properties import LoggingProperties
logger = logging.getLogger('shared.logging.logger')  # the class is singleton and gets the logger with azure log handler


async def exception_callback(request: Request, exc: Exception):
    logger.exception(exc)
    return JSONResponse({"detail": "Internal server error"}, status_code=HTTP_500_INTERNAL_SERVER_ERROR)
