from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root() -> dict[str, str]:
    return {"result": "Hello, World"}


@router.get("/health")
async def read_health() -> dict[str, str]:
    return {"status": "ok"}
