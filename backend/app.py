import os
from typing import List

import uvicorn
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

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


# For more details consider https://github.com/mongodb-developer/mongodb-with-fastapi/blob/master/app.py
if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)
