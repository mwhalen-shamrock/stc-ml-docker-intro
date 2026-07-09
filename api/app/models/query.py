from typing import Any

from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str = Field(..., description="SQL query to execute")
    args: list[str] | None = Field(default=None, description="Values for $1, $2, ...")


class QueryResponse(BaseModel):
    row_count: int
    rows: list[dict[str, Any]]
