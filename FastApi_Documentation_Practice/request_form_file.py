"""
Request Forms and Files
You can define files and form fields at the same time using File and Form.
"""

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.post("/files/")
async def create_file(
        file:Annotated[bytes, File()],
        fileb:Annotated[UploadFile, File()],
        token:Annotated[str,Form()],

):
    return {
        "file_size": len(file),
        "fileb_content_type":fileb.content_type,
        "token":token,
    }