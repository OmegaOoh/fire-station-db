"""URL configuration for fire station app."""
from django.urls import path
from . import views
from .choice_enum import get_choice

app_name = "fire-station"
urlpatterns = [
    path("", views.FireStationView.as_view(), name="station-list"),
    path("<int:pk>/", views.FireStationDetailView.as_view(), name="station-list"),
    path("staff/", views.StaffList.as_view(), name="station-list"),
    path("choice/", get_choice, name="station-list"),
    path("equipments/", views.EquipmentsView.as_view(), name="equipments"),
    path("fire-engine/", views.FireEngineView.as_view(), name="fire-engine"),
]
