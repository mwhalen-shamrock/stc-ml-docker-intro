from fastapi import APIRouter

from app.models import PredictionRequest, PredictionResponse

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(payload: PredictionRequest) -> PredictionResponse:
    _ = payload
    return PredictionResponse(result=42.0)
