from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

MONGO_URI = settings.MONGO_URI
MONGO_NAME = settings.MONGO_NAME

def get_sync_db_client():
    client = MongoClient(MONGO_URI, tlsAllowInvalidCertificates=True)
    return client[MONGO_NAME]

async def get_async_db_client():
    client = AsyncIOMotorClient(MONGO_URI, tlsAllowInvalidCertificates=True)
    return client[MONGO_NAME]

async def get_media_collection():
    db = await get_async_db_client()
    return db["media"]
