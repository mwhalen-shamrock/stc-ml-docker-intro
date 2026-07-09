from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    feature_a: float = Field(..., description="Example numeric feature")
    feature_b: float = Field(..., description="Example numeric feature")


class PredictionResponse(BaseModel):
    result: float = Field(..., description="Predicted value")
