from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: Annotated[int, Path(title= " Item Description",ge=1, le=100)],
                     q:str,
                     size: Annotated[float,Query(gt=1.0,lt=50.50)]):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    if size:
        results.update({"size":size})
    return results
