from enum import Enum

# Enum for Gender
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"