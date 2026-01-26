from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def get_database():
    if db.client is None:
        db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    return db.client[settings.PROJECT_NAME.lower().replace(" ", "")]

async def close_mongo_connection():
    if db.client:
        db.client.close()
