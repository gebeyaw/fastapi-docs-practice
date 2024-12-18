"""Data access methods for roles"""
from typing import List, Optional
from User_Management.Models.Role import Role

# Simulating a database with an in-memory list for demonstration purposes.
FAKE_ROLE_DB: List[Role] = [
    Role.OPERATION_MANAGER,
    Role.GENERAL_MANAGER,
    Role.ADMIN,
    Role.SALES_OFFICER,
    Role.STOREKEEPER,
    Role.FINANCE_PERSONAL,
    Role.FULFILLMENT_SUPERVISOR,
    Role.DELIVERY_AGENT,
]


class RoleRepository:
    @classmethod
    def get_all_roles(cls) -> List[Role]:
        """Returns a copy of all roles."""
        return FAKE_ROLE_DB.copy()

    @classmethod
    def get_role(cls, role_name: str) -> Optional[Role]:
        """Finds a role by its name."""
        return next((role for role in FAKE_ROLE_DB if role == role_name), None)