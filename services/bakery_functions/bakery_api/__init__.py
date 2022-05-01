from typing import Dict
import json
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from injector import Injector, singleton
from starlette.middleware.cors import CORSMiddleware
from fastapi import Request

from bakery.application.exception.bakery_exception import BakeryException
from bakery.constant import Constant
from shared.application.middleware import generic_exception_logging
from shared.application.middleware.azure_request_logging import request_logging
from shared.logging.logger import Logger
from shared.reader.config_reader import ConfigReader
from shared.integration.mediator import Mediator

injector = Injector()
account_name = ConfigReader.read_config_parameter('storage_account_name')
account_key = ConfigReader.read_config_parameter('storage_account_key')
conn_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};" \
              f"AccountKey={account_key};" \
              f"EndpointSuffix=core.windows.net"
cdn_name = ConfigReader.read_config_parameter(Constant.ConfigKey.CDN_NAME)

log_instrumentation_key = ConfigReader.read_config_parameter(Constant.ConfigKey.LOG_INSTRUMENTATION_KEY)
injector.binder.bind(Logger, to=Logger(log_instrumentation_key=log_instrumentation_key), scope=singleton)

router = APIRouter(
    prefix="/api/v1",
    responses={404: {"description": "Not found"}},
)

app = FastAPI(title='Bakery API',
              description='API ENDPOINTS')

from bakery_api.controller import ka_router

app.include_router(ka_router)


@app.exception_handler(BakeryException)
async def project_exception_handler(request: Request, exc: BakeryException):
    return JSONResponse(status_code=exc.status_code, content=exc.message)


origins = json.loads(ConfigReader.read_config_parameter(Constant.ConfigKey.CORS_ORIGINS))


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware('http')(request_logging)
app.exception_handler(Exception)(generic_exception_logging.exception_callback)

Mediator.injector = injector
