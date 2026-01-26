from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_medications():
    return []

@router.post("/")
async def create_medication():
    return {"message": "Medication created"}
