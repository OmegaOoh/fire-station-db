from django.db import models


class DayOfWeek(models.IntegerChoices):
    """ENUM represent day of weeks"""
    MONDAY = 1, "Monday"
    TUESDAY = 2, "Tuesday"
    WEDNESDAY = 3, "Wednesday"
    THURSDAY = 4, "Thursday"
    FRIDAY = 5, "Friday"
    SATURDAY = 6, "Saturday"
    SUNDAY = 7, "Sunday "


class Gender(models.TextChoices):
    Male = "Male", "Male"
    Female = "Female", "Female"
    Other = "Other"


class FireFighterRank(models.IntegerChoices):
    """Ranks of Firefighter (ascending order)."""
    FIRE_FIGHTER = 1, "FireFighter"
    ENGINEER = 2, "Engineer"
    LIEUTENANT = 3, "Lieutenant"
    CAPTAIN = 4, "Captain"
    DISTRICT_CHIEF = 5, "District Chief"
    DIVISION_CHIEF = 6, "Division Chief"
    DEPUTY_FIRE_CHIEF = 7, "Deputy Fire Chief"
    FIRE_CHIEF = 8, "Fire Chief"


class FireFighterRole(models.TextChoices):
    """Fire Fighter Field Role"""
    Commander = "Incident Commander", "Incident Commander"
    COMPANY_OFFICER = "Company Officer", "Company Officer"
    HOSELINE_OPERATOR = "Hoseline Operator", "Hoseline Operator"
    NOZZLE_OPERATOR = "Nozzle Operator", "Nozzle Operator"
    VENT_TECHNICIAN = "Vent Technician", "Vent Technician"
    SEARCH_AND_RESCUE = "Search and Rescue", "Search and Rescue Technician"
    MEDICAL = "Medic", "Medical Technician"


class IncidentType(models.IntegerChoices):
    """Type of Incident."""
    STRUCTURE_FIRE = 1, "Structure Fire"
    WILD_FIRE = 2, "Wild Fire"
    VEHICLE_FIRE = 3, "Vehicle Fire"
    HAZMAT_FIRE = 4, "Hazmat Fire"
    MEDICAL_EMERGENCY = 5, "Medical Emergency"
    VEHICLE_ACCIDENT = 6, "Vehicle Accident"
    WATER_RESCUE = 7, "Water Rescue"
    HAZMAT_INCIDENT = 8, "Hazmat Accident"
    NATURAL_DISASTER = 9, "Natural Disaster"
    TECHNICAL_RESCUE = 10, "Technical Rescue"
