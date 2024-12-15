"""
Extra Models
It will be common to have more than one related model.

This is especially the case for user models, because:
- The input model needs to be able to have a password.
- The output model should not have a password.
- The database model would probably need to have a hashed password.
Never store user's plaintext passwords. Always store a "secure hash" that you can then verify.
"""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    fullname: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    hashed_password = "supersecret" + raw_password
    return hashed_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserDB(**user_in.model_dump(), hashed_password= hashed_password)
    print("The user is successfully saved!")
    return user_in_db


@app.post("/user/", response_model= UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved







