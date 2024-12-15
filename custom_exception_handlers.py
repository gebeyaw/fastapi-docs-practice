"""
custom exception handlers
You can add custom exception handlers with the same exception utilities from Starlette.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class UvicornException(Exception):
    def __init__(self, name:str):
        self.name = name


app = FastAPI()


@app.exception_handler(UvicornException)
async def unicorn_exception_handler(request: Request, exc:UvicornException):
    return JSONResponse (
        status_code= 418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/uvicorn/{name}")
async def read_item(name:str):
    if name == "Yolo":
        raise UvicornException(name)
    return {"uvicorn_name": name}
