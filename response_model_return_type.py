"""
Response Model - Return Type
You can declare the type used for the response by annotating the path operation function return type.
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] | None = None

@app.post("/items/")
async def create_items(item:Item) ->Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name = "laptop", price = 350),
        Item(name = "desktop", price = 500)
    ]