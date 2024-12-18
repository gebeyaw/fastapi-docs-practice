"""Manages role-related requests"""
from fastapi import APIRouter, HTTPException
from typing import List
from User_Management.Services.RoleService import RoleService
from User_Management.Models.Role import Role  # Assuming Role is defined in a Models package

# Extracted constant for the base route
ROLES_API_ROUTE = "/roles/"

router = APIRouter()


@router.get(ROLES_API_ROUTE, response_model=List[Role])  # Updated to use Role enum
def get_roles() -> List[Role]:  # Added explicit type hints
    # Ensures returned roles are enums, improving clarity and validation
    try:
        return [Role(role_dict["name"]) for role_dict in RoleService.list_roles()]
    except KeyError:
        raise HTTPException(status_code=500, detail="Invalid role data format encountered")