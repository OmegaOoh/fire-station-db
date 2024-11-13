import enum


class DayOfWeek(enum.Enum):
    """ENUM represent day of weeks"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class FireFighterRank(enum.Enum):
    """Ranks of Firefighter (ascending order)."""
    FIRE_FIGHTER = 'FireFighter'
    ENGINEER = "Engineer"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    DISTRICT_CHIEF = "District Chief"
    DIVISION_CHIEF = "Division Chief"
    DEPUTY_FIRE_CHIEF = "Deputy Fire Chief"
    FIRE_CHIEF = "Fire Chief"


class FireFighterRole(enum.Enum):
    """Fire Fighter Field Role"""
    Commander = "Incident Commander"
    COMPANY_OFFICER = "Company Officer"
    HOSELINE_OPERATOR = "Hoseline Operator"
    NOZZLE_OPERATOR = "Nozzle Operator"
    VENT_TECHNICIAN = "Vent Technician"
    SEARCH_AND_RESCUE = "Search and Rescue Technician"
    MEDICAL = "Medical Technician"


class IncidentType(enum.Enum):
    """Type of Incident."""
    STRUCTURE_FIRE = 1
    WILDLAND_FIRE = 2
    VEHICLE_FIRE = 3
    HAZMAT_FIRE = 4
    MEDICAL_EMERGENCY = 5
    VEHICLE_ACCIDENT = 6
    WATER_RESCUE = 7
    HAZMAT_INCIDENT = 8
    NATURAL_DISASTER = 9
    TECHNICAL_RESCUE = 10
