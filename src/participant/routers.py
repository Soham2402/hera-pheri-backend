from fastapi import APIRouter, Depends, HTTPException

from src.database import PARTICIPANT_COLLECTION, create_document
from src.participant import utils
from src.utils import get_database_dependency
from src.participant.schema import CreateParticpantResponseSchema

router = APIRouter(
    prefix="/participant",
    tags=["get_participant", "create_participant"]
)


@router.post("/create_participant")
async def create_participant(db=Depends(get_database_dependency)):
    new_user: object = utils.generate_new_participant(room_id=None)
    result = await create_document(model_instance=new_user,
                                   collection_name=PARTICIPANT_COLLECTION,
                                   db=db)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])

    response_data = {
        **result["data"],
        "id": result["id"]
    }
    return CreateParticpantResponseSchema(**response_data)
