from django.db import models
from django.utils import timezone
from .choice_enum import DayOfWeek, FireFighterRank, FireFighterRole, IncidentType, Gender
from django_enum import EnumField


class Station(models.Model):
    """Station Information. Capacity and Address"""
    station_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    staff_capacity = models.IntegerField()
    fire_engine_capacity = models.IntegerField()

    def __str__(self) -> str:
        return self.station_name


class Shift(models.Model):
    """Working Shift indicates, Start time, End time and day of weeks."""
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    day = EnumField(DayOfWeek)

    def __str__(self):
        return f"{self.day}, {self.shift_start} - {self.shift_end}"


class Staff(models.Model):
    """Fire Station Staff."""
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = EnumField(Gender)
    position = models.CharField(max_length=100)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    # Make shift optional until shift serializer done
    shift = models.ManyToManyField(Shift, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    @property
    def is_fire_fighter(self):
        """Tell whether staff are fire fighter or not"""
        return hasattr(self, 'firefighter')


class FireFighter(models.Model):
    """Firefighter is also Staff"""
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    rank = EnumField(FireFighterRank)
    role = EnumField(FireFighterRole)

    def __str__(self):
        return f"{self.rank}.{self.staff}, {self.role}"


class Equipment(models.Model):
    """Equipment/ Tools"""
    item_name = models.CharField(max_length=100)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.item_name}"


class FireEngine(models.Model):
    """FireEngine (Firetruck)"""
    engine_number = models.IntegerField()
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=10)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"{self.model} license plate: {self.license_plate}"


class Dispatch(models.Model):
    """Info of dispatch"""
    incident = EnumField(IncidentType)
    reported_time = models.DateTimeField(default=timezone.now)
    notified_time = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=250)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    fire_engine = models.ManyToManyField(FireEngine)
    equipment_used = models.ManyToManyField(Equipment)
    fire_fighter = models.ManyToManyField(FireFighter)
    resolved_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.incident} at {self.address}, {self.reported_time}"
