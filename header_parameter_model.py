"""
If you have a group of related header parameters, you can create a Pydantic model to declare them.
Declare the header parameters that you need in a Pydantic model, and then declare the parameter as Header
In some special use cases (probably not very common), you might want to restrict the headers that you want
to receive.
You can use Pydantic's model configuration to forbid any extra fields
"""

from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()

class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    trace_parent: str | None = None
    x_tag: list[str]


@app.get("/items/")
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers