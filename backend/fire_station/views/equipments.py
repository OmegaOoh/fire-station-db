"""Module for handle equipments."""
from typing import Any
from django.http import HttpRequest
from django.db.models import QuerySet
from rest_framework import generics, mixins, response, status
from fire_station import models, serializer


class EquipmentsView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """Return list of the equipments when GET request and create new equipments when POST request."""

    serializer_class = serializer.EquipmentSerializer

    def get_queryset(self) -> QuerySet:
        """Equipments view return list of usable equipment (Not on board yet)."""
        return models.Equipment.objects.filter(fireengine__isnull=True)

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by return with list of equipments.

        :param request: Http request object
        :return: Http response object
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle post request by creating equipments and return list of equipments.

        :param request: Http request object
        :return: Http response object
        """
        self.create(request, *args, **kwargs)

        serializer = self.get_serializer(self.get_queryset(), many=True)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle delete request by deleting equipments and return list of equipments.

        :param request: Http request object
        :return: Http response object
        """
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Get equipments instance and destroy it.

        :param request: Http request object
        :return: Http response object
        """
        queryset = self.get_queryset()
        equipments_id = self.request.GET.get("equipments_to_remove", [])
        equipments_to_remove = queryset.filter(id__in=equipments_id)
        self.perform_destroy(equipments_to_remove)

        serializer = self.get_serializer(self.get_queryset(), many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)
