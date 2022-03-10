import os
from typing import List

import uvicorn
from fastapi import FastAPI, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from models.health import HealthModel
from models.item import ItemModel, UpdateItemModel

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(db_url)
db = client.items


@app.get(
    "/api/health",
)
async def list_items() -> HealthModel:
    version = os.getenv('VERSION', 'unknown')
    return HealthModel(status='OK', version=version)


@app.get(
    "/api/items",
    response_description="List all items",
    response_model=List[ItemModel],
    response_model_by_alias=False,
)
async def list_items() -> List[ItemModel]:
    result = []
    for raw_data_item in await db["items_collection"].find().to_list(1000):
        result.append(ItemModel(**raw_data_item))
    return result


@app.post(
    "/api/items",
    response_description="Add new item",
    response_model=ItemModel,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
async def create_item(item: ItemModel = Body(...)) -> ItemModel:
    item = jsonable_encoder(item)
    new_item = await db["items_collection"].insert_one(item)
    created_item = await db["items_collection"].find_one({"_id": new_item.inserted_id})
    return ItemModel(**created_item)


@app.put(
    "/api/items/{_id}",
    response_description="Update item",
    response_model=ItemModel,
    response_model_by_alias=False,
)
async def update_item(_id: str, item: UpdateItemModel = Body(...)) -> ItemModel:
    item_dict = {k: v for k, v in item.dict().items() if v is not None}

    if len(item_dict) >= 1:
        update_result = await db["items_collection"].update_one(
            {"_id": _id}, {"$set": item_dict}
        )

        if update_result.modified_count == 1:
            if (
                updated_item := await db["items_collection"].find_one({"_id": _id})
            ) is not None:
                return updated_item

    if (
        existing_item := await db["items_collection"].find_one({"_id": _id})
    ) is not None:
        return existing_item

    raise HTTPException(status_code=404, detail=f"Item {_id} not found")


# For more details consider https://github.com/mongodb-developer/mongodb-with-fastapi/blob/master/app.py
if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=9000, reload=True)
