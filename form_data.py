"""
Form Data
When you need to receive form fields instead of JSON, you can use Form.
To declare form bodies, you need to use Form explicitly, because without it the parameters
would be interpreted as query parameters or body (JSON) parameters.
"""
from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def user_login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"Username":username}


