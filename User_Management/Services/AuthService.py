"""Business logic related to authentication"""
from User_Management.Repositories.UserRepository import UserRepository
from User_Management.Models.User import User
from typing import Optional


class AuthService:
    @staticmethod
    def verify_credentials(username: str, password: str) -> bool:
        user: Optional[User] = UserRepository.get_user_by_username(username)
        if user and AuthService._verify_password(password, user.password):
            return True
        return False

    @staticmethod
    def _verify_password(input_password: str, stored_password_hash: str) -> bool:
        # Note: In production, passwords should always be hashed and verified using a secure method.
        # Example: Use bcrypt or Argon2 for password hashing/verification.
        return input_password == stored_password_hash