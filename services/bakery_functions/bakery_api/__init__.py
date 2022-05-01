from fastapi import FastAPI, APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
from injector import Injector
from starlette.middleware.cors import CORSMiddleware

from bakery.application.exception.bakery_exception import BakeryException
from shared.application.middleware import generic_exception_logging
from shared.application.middleware.request_logging import request_logging
from shared.integration.mediator import Mediator

injector = Injector()

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


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware('http')(request_logging)
app.exception_handler(Exception)(generic_exception_logging.exception_callback)

Mediator.injector = injector
