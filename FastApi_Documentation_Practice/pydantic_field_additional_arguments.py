from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str = Field(examples= ["Laptop"])
    description:str | None = Field(default= None, examples= ["a very good item"])
    price:float = Field(examples= [34.5])
    tax:float | None = Field(default= None, examples= [1.3])

@app.put("/item/{item_id}")
async def update_item(item_id: int, item:Item):
    result = {"item_id":item_id, "item":item}
    return result