from User_Management.Models.User import User
from User_Management.Repositories.UserRepository import UserRepository

# A constant for returning an empty list, if needed in the business flow.
EMPTY_USER_LIST = []


class UserService:
    @staticmethod
    def register_user(user_data: User) -> User:
        """Registers a new user"""
        return UserRepository.create_user(user_data)

    @staticmethod
    def get_user_by_username(username: str) -> User:
        """Finds a user by their username"""
        return UserRepository.get_user_by_username(username)

    @staticmethod
    def get_all_users() -> list[User]:
        """Lists all registered users"""
        return UserRepository.get_all_users() or EMPTY_USER_LIST