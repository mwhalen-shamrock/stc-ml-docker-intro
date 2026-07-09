from collections.abc import Sequence

import asyncpg


async def run_query(
    pool: asyncpg.Pool,
    query: str,
    params: Sequence[str] | None = None,
) -> list[dict[str, object]]:
    values = list(params or [])

    async with pool.acquire() as connection:
        rows = await connection.fetch(query, *values)

    return [dict(row) for row in rows]
