import os
from typing import List

import uvicorn
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from starlette import status
from starlette.responses import JSONResponse, Response

from backend.models.item import ItemModel

app = FastAPI()
db_url = os.getenv('MONGODB_URL', 'mongodb://localhost:27017')
client = AsyncIOMotorClient(db_url)
db = client.items


@app.get(
    '/api/items', response_description='List all items', response_model=List[ItemModel], response_model_by_alias=False,
)
async def list_items() -> List[ItemModel]:
    result = []
    for raw_data_item in await db['items_collection'].find().to_list(1000):
        result.append(ItemModel(**raw_data_item))
    return result


@app.post('/api/items', response_description='Add new item', response_model=ItemModel, response_model_by_alias=False,
          status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemModel = Body(...)) -> ItemModel:
    item = jsonable_encoder(item)
    new_item = await db['items_collection'].insert_one(item)
    created_item = await db['items_collection'].find_one({'_id': new_item.inserted_id})
    return ItemModel(**created_item)


# For more details consider https://github.com/mongodb-developer/mongodb-with-fastapi/blob/master/app.py
if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)
