# Fill in other mock endpoints to avoid import errors
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
async def root(): return []
