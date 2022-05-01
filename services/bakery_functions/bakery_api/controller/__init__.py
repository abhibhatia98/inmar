from fastapi import APIRouter

from bakery_api.controller.location_controller import router as bakery_router


ka_router = APIRouter()
ka_router.include_router(bakery_router)
