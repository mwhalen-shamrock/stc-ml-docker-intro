import asyncpg
from fastapi import APIRouter, HTTPException, Request

from app.core.database import run_query
from app.models import QueryRequest, QueryResponse

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def query_database(
    request: Request,
    payload: QueryRequest,
) -> QueryResponse:
    query = payload.query

    if not query.lstrip().lower().startswith("select"):
        raise HTTPException(status_code=400, detail="Only SELECT queries are allowed")

    pool = request.app.state.db_pool

    try:
        rows = await run_query(pool=pool, query=query, params=payload.args)
    except asyncpg.PostgresError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return QueryResponse(row_count=len(rows), rows=rows)
