from enum import Enum

# Enums for hierarchy
class Country(str, Enum):
    ETHIOPIA = "Ethiopia"

class Region(str, Enum):
    ADDIS_ABABA = "Addis Ababa"
    OROMIA = "Oromia"
    AMHARA = "Amhara"
    TIGRAY = "Tigray"
    SNNPR = "Southern Nations, Nationalities, and Peoples' Region"

class Zone(str, Enum):
    ARADA = "Arada"
    KIRKOS = "Kirkos"
    BOLE = "Bole"
    GULELE = "Gulele"

class Woreda(str, Enum):
    WOREDA_1 = "Woreda 1"
    WOREDA_2 = "Woreda 2"
    WOREDA_3 = "Woreda 3"