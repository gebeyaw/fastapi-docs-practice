from enum import Enum

class EducationLevel(str, Enum):
    NO_EDUCATION = "No education"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    DIPLOMA = "Diploma"
    BACHELOR = "Bachelor"
    MASTERS = "Masters"
    PHD = "PhD"