"""Handles HTTP requests related to users"""
from fastapi import APIRouter, HTTPException
from User_Management.Models.User import User
from User_Management.Services.UserService import UserService

router = APIRouter()


def handle_user_not_found(user: User, username: str) -> User:
    """Raise an HTTPException if the user is not found"""
    if not user:
        raise HTTPException(status_code=404, detail=f"User with username '{username}' not found")
    return user


@router.post("/users/", response_model=User)
def create_user(user: User):
    """Endpoint to create a new user"""
    return UserService.register_user(user)


@router.get("/users/{username}", response_model=User)
def get_user_by_username(username: str):
    """Endpoint to get user by username"""
    user = UserService.get_user_by_username(username)
    return handle_user_not_found(user, username)


@router.get("/users/", response_model=list[User])
def get_all_users():
    """Endpoint to list all users"""
    return UserService.get_all_users()