from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/item/{item_id}", response_model=Item)
async def update_item(
        *,
        item_id: int,
        item: Annotated[
            Item,
            Body(
                examples= [

                    {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,

                    },
                    {
                        "name": "laptop",
                        "price": 1500,
                        "tax":150,
                    },
                    {
                        "name": "Oil",
                        "price":100,
                    },
                ],
            ),
        ],
        ):
    result = {"item_id":item_id, "item":item}
    return result