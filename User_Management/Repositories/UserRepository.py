"""Data access methods for users"""
from typing import List, Optional, TypeAlias
from User_Management.Models.User import User

# Type alias for clarity and consistency
UserList: TypeAlias = List[User]

# Simulating a database with an in-memory list for demonstration purposes.
in_memory_user_db: UserList = []


class UserRepository:
    @classmethod
    def _find_user_by_username(cls, username: str) -> Optional[User]:
        """Private helper method to find a user by username"""
        return next((user for user in in_memory_user_db if user.username == username), None)

    @classmethod
    def create_user(cls, user: User) -> User:
        """Adds a new user to the in-memory database"""
        in_memory_user_db.append(user)
        return user

    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[User]:
        """Fetches a user by username"""
        return cls._find_user_by_username(username)

    @classmethod
    def get_all_users(cls) -> UserList:
        """Returns a copy of all users in the database"""
        return in_memory_user_db.copy()