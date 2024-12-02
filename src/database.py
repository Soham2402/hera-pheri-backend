from typing import Any, Dict, TypeVar


from datetime import datetime
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from src.constants import settings

CLIENT = AsyncIOMotorClient(settings.mongo_uri)
DB_NAME = CLIENT[settings.db_name]

PARTICIPANT_COLLECTION = "participants"


model_type = TypeVar('T', bound=BaseModel)


async def create_document(model_instance: model_type,
                          collection_name: str,
                          db: AsyncIOMotorClient) -> Dict[str, Any]:
    """A generic function which can be used to insert a document into a collection

    Args:
        model_instance (model_type): The data which has to be inserted, it should be a pydantic obj
        collection_name (str): The name of the collection in which the data has to be inserted in
        db (AsyncIOMotorClient): The database dependency in which the collection exists

    Raises:
        Exception: This needs to be flushed out

    Returns:
        Dict[str, Any]: _description_
    """
    
    try:
        document = model_instance.model_dump(exclude_defaults=True)
        current_timestamp = datetime.now()
        document["created_at"] = current_timestamp
        document["modified_at"] = current_timestamp

        collection = db[collection_name]
        result = await collection.insert_one(document)

        if not result.inserted_id:
            raise Exception("Failed to insert document, insert_id not found")

        return {"id": str(result.inserted_id),
                "message": f"{collection_name.title()} document created",
                "data": document,
                "status": "success"}

    except Exception as e:
        logging.error(f"Error while creating a record==> {str(e)}")
        return {
            "message": f"Error creating {collection_name} document: {str(e)}",
            "status": "error",
            "error": str(e)
        }
