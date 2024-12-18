from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    userName: str
    fullName: str| None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    user: User,
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id, "User":user}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results