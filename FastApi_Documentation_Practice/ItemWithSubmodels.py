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
    tags: Set[str]
    images:list[Image] | None = None


class Offer(BaseModel):
    name:str
    description: str | None = None
    Price: float
    items: list[Item]


app = FastAPI()


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer