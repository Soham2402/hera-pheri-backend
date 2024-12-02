from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ParticipantSchema(BaseModel):
    username: str = Field(description="must be a string and is required")
    user_rooms: List[str] = Field(description="must be an array")
    is_active: bool = Field(True,
                            description="must be a boolean and is required")

    class Config:
        json_schema_extra = {
            "example": {
                "username": "test_user",
                "user_rooms": ["testroomid1", "testroomid2"],
                "is_active": "true"
            }
        }
        from_attributes = True


class CreateParticpantResponseSchema(ParticipantSchema):
    id: str
    created_at: datetime
    modified_at: Optional[datetime] = None
