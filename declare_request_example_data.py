from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None
    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                    "name": "Laptop",
                    "description":"A very good item",
                    "price":34.5,
                    "tax":1.3,
                }
            ]
        }
    }
@app.put("/item/{item_id}")
async def update_item(item_id:int, item:Item):
    result = {"item_id":item_id,"item":item}
    return result