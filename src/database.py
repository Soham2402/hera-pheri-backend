from motor.motor_asyncio import AsyncIOMotorClient

from src.constants import settings

CLIENT = AsyncIOMotorClient(settings.mongo_uri)
DB_NAME = CLIENT[settings.db_name]
