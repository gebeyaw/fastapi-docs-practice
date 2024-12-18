"""Defines the User model/schema"""
from .Role import Role
from .WorkingAreaLevel import WorkingAreaLevel
from .Gender import Gender
from .EducationLevel import EducationLevel


from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username: str = Field(..., min_length=3)
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int = Field(..., ge=18)
    gender: Gender
    education_level: EducationLevel
    email: EmailStr
    password: str = Field(..., min_length=8)

    # Role and hierarchical fields
    role: Role

    # Working area level and corresponding value
    working_area_level: WorkingAreaLevel
    working_area_value: str # This will hold the specific value based on the selected level
