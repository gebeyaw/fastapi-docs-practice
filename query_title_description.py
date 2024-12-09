from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
            include_in_schema=False
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


"""
Alias parameters
Imagine that you want the parameter to be item-query.

Like in:
http://127.0.0.1:8000/items/?item-query=foobaritems


Deprecating parameters
You don't like this query parameter anymore.

You have to leave it there a while because there are clients using it, 
but you want the docs to clearly show it as deprecated.

Then pass the parameter deprecated=True to Query


Exclude parameters from OpenAPI
To exclude a query parameter from the generated OpenAPI schema 
(and thus, from the automatic documentation systems), 
set the parameter include_in_schema of Query to False

"""