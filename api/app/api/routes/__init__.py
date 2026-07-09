from fastapi import APIRouter

from app.api.routes.basic import router as basic_router
from app.api.routes.database import router as database_router
from app.api.routes.prediction import router as prediction_router

api_router = APIRouter()
api_router.include_router(basic_router)
api_router.include_router(database_router)
api_router.include_router(prediction_router)
