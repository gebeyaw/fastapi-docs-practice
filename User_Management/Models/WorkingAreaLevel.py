from enum import Enum
# Enum for working area level
class WorkingAreaLevel(str, Enum):
    COUNTRY = "country"
    REGION = "region"
    ZONE = "zone"
    WOREDA = "woreda"