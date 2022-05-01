import logging
from starlette.requests import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from shared.logging.custom_dimension import CustomDimension
from shared.logging.logging_properties import LoggingProperties
logger = logging.getLogger('shared.logging.logger')  # the class is singleton and gets the logger with azure log handler


async def exception_callback(request: Request, exc: Exception):
    pass
    # custom_dimension = CustomDimension(trace_id=request.headers.get('trace_id'),
    #                                    organization_id=request.path_params.get("organization_id", "UNPROTECTED_ROUTE"),
    #                                    project_id=request.path_params.get("project_id", "PROJECT_ID_NA"),
    #                                    master_category_id=request.path_params.get("category_id", "MASTER_CATEGORY_ID_NA"),
    #                                    request_url=str(request.url))
    # logg_props = LoggingProperties(custom_dimensions=custom_dimension)
    # logger.exception("EXCEPTION", extra=logg_props.dict())
    # return JSONResponse({"detail": "Internal server error"}, status_code=HTTP_500_INTERNAL_SERVER_ERROR)
