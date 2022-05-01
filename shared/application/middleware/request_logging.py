import logging
from starlette.requests import Request

logger = logging.getLogger("shared.logging.logger")

async def request_logging(request: Request, call_next):
    return await call_next(request)