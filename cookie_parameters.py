from fastapi import FastAPI,Cookie
from typing import Annotated

app = FastAPI()


@app.get("/item/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}