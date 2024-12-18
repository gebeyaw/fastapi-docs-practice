"""
Cookie Parameter Models
If you have a group of cookies that are related, you can create a Pydantic model to declare them.

This would allow you to re-use the model in multiple places and also to declare validations
and metadata for all the parameters at once.
"""

"""
Cookies with a Pydantic Model
Declare the cookie parameters that you need in a Pydantic model, and then declare the parameter as Cookie
"""

"""
Forbid Extra Cookies
In some special use cases (probably not very common), you might want to restrict the cookies that you want 
to receive.
You can use Pydantic's model configuration to forbid any extra fields:
"""

from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Cookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
