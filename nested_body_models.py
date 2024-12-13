from typing import Set
from fastapi import FastAPI
from pydantic import BaseModel


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None
    tags: Set[str]
    images: Image | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

