"""URL configuration for fire station app."""
from django.urls import path
from . import views
from .choice_enum import get_choice

app_name = "fire-station"
urlpatterns = [
    path("", views.FireStationView.as_view(), name="station-list"),
    path("<int:pk>/", views.FireStationDetailView.as_view(), name="station-list"),
    path("choice/", get_choice, name="station-list"),
    path("shift/", views.ShiftView.as_view(), name='shift-list'),
    path("shift/<int:pk>/", views.ShiftChangeView.as_view(), name='shift-change')
]
