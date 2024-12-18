"""
Handling Errors
There are many situations in which you need to notify an error to a client that is using your API.
"""
from typing import Annotated
from fastapi import FastAPI, HTTPException

app =  FastAPI()

items = {"foo": "Electronic Devices", "zoo": "Animals"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException (status_code= 404, detail="Item not Found")

    return {"item":items[item_id]}


