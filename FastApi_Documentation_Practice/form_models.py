"""
Form Models
You can use Pydantic models to declare form fields in FastAPI.

Pydantic Models for Forms
You just need to declare a Pydantic model with the fields you want to receive as form fields,
and then declare the parameter as Form:
"""

from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

class FormData(BaseModel):
    username: str
    password:str

app = FastAPI()

@app.post("/login/")
async def user_login(data: Annotated[FormData, Form()]):
    return data


