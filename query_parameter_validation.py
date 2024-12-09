from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=10, pattern= "^fixedquery$")] = None):
    results=  {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})

    return  results


"""You can use default values other than None"""
"""async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):"""

"""when you need to declare a value as required while using Query, you can simply not declare a default value"""
"""async def read_items(q: Annotated[str, Query(min_length=3)])"""

"""Required with Ellipsis (...)
There's an alternative way to explicitly declare that a value is required. 
You can set the default to the literal value ... as follow
"""
"""async def read_items(q:Annotated[str, Query(min_length =3 )] = ...)"""


"""Required, can be None
You can declare that a parameter can accept None, but that it's still required. 
This would force clients to send a value, even if the value is None."""

"""async def read_items(q:Annotated[str | None, Query(min_length = 3)]= ...)"""