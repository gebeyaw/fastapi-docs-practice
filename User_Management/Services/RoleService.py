"""Business logic related to roles"""
from typing import List, Optional
from User_Management.Repositories.RoleRepository import RoleRepository


class RoleService:
    def __init__(self, role_repository: RoleRepository):
        # Use dependency injection to make the service more testable and decoupled
        self.role_repository = role_repository

    def list_roles(self) -> List[dict]:  # Assuming roles are returned as dictionaries
        try:
            return self.role_repository.get_all_roles()
        except Exception as e:
            # Add error handling
            print(f"Error fetching roles: {str(e)}")  # Replace with a logging statement
            return []

    def find_role(self, role_name: str) -> Optional[dict]:  # Adjusted return type hint
        try:
            role = self.role_repository.get_role(role_name)
            if not role:
                print(f"Role '{role_name}' not found")  # Replace with a logging statement
            return role
        except Exception as e:
            # Add error handling
            print(f"Error finding role '{role_name}': {str(e)}")  # Replace with a logging statement
            return None
