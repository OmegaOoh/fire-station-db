"""URL configuration for fire station app."""
from django.urls import path
from . import views

app_name = "fire-station"
urlpatterns = [
    path("", views.FireStationView.as_view(), name="station-list"),
    path("<int:pk>/", views.FireStationDetailView.as_view(), name="station-list")
]
