"""URL configuration for fire station app."""
from django.urls import path
from . import views

app_name = "fire-station"
urlpatterns = [
    path("check", views.test_view, name="test"),
    path("equipments/", views.EquipmentsView.as_view(), name="equipments"),
]
