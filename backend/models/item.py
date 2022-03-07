from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from models import PyObjectId


def replace_id(arg: str) -> str:
    return arg.replace("_id", "id")


class ItemModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    value: str = Field(...)
    completed: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "61dead6c2c3778a9f656beaf",
                "value": "Some item to complete",
                "completed": False,
            }
        }


class UpdateItemModel(BaseModel):
    value: Optional[str]
    completed: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "value": "Some item to complete",
                "completed": False,
            }
        }
