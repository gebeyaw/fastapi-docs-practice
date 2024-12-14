"""
response_model Parameter¶
There are some cases where you need or want to return some data that is not exactly what the type declares.

For example, you could want to return a dictionary or a database object, but declare it as a Pydantic model.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any


app = FastAPI()

class Item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float | None = None
    tags:list[str] | None = None

@app.post("/items/",response_model=Item)
async def create_items(item:Item) -> Any:
    return item

@app.get("/items/", response_model= list[Item])
async def read_items() -> Any:
    return [
        {"name": "Popcorn", "price": 123.50},
        {"name": "corn", "price": 50},
    ]

