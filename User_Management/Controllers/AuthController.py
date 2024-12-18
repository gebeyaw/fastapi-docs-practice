"""Manages authentication processes"""
from fastapi import APIRouter, HTTPException
from User_Management.Services.AuthService import AuthService

router = APIRouter()


def authenticate_user(username: str, password: str):
    """Handles user authentication logic."""
    if not AuthService.verify_credentials(username, password):
        raise HTTPException(status_code=401, detail="Invalid username or password")


@router.post("/auth/login/")
def login(username: str, password: str):
    authenticate_user(username, password)
    return {"message": "Login successful"}