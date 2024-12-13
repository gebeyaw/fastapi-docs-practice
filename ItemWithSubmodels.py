from typing import Set
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name:str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str]
    images:Set[Image]


app = FastAPI()


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id":item_id, "item":item}
    return result