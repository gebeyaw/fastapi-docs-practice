from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

"""Query parameter list / multiple values with defaults"""

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = ["foo","buz"]):
    query_items = {"q": q}
    return query_items


"""You can also use list directly instead of List[str] (or list[str] in Python 3.9+)
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items
"""


"""You can add a title and description for query parameter
async def read_items(
          q:Annotated [str | None, 
          Query(title = "Query string", 
                description = "Query string for the items to search in the database that have a good match",
                min_length=3)] = none):
                                       results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
                                       if q:
                                           results.update({"q": q})
                                       return results
"""