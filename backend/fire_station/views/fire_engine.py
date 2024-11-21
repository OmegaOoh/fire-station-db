"""Module for handle fire engines."""
from typing import Any
from django.http import HttpRequest
from django.db.models import QuerySet
from rest_framework import generics, mixins, response, status
from fire_station import models, serializer


class FireEngineView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    """Return list of the fire engines when GET request."""

    serializer_class = serializer.FireEngineSerializer

    def get_queryset(self) -> QuerySet:
        """FireEngine view return list of fire engines."""
        return models.FireEngine.objects.all()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by return with list of fire engines.

        :param request: Http request object
        :return: Http response object
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle post request by creating fire engines and return list of fire engines.

        :param request: Http request object
        :return: Http response object
        """
        fire_engine_id = request.data.get('id')

        if self.get_queryset().filter(id=fire_engine_id).exists():
            return self.update(request, *args, **kwargs)
        else:
            # Check if number of fire engines exceed the capacity
            res = self.__check_fire_engine_capacity(request, *args, **kwargs)
            if res:
                return res

            self.create(request, *args, **kwargs)

            serializer = self.get_serializer(self.get_queryset(), many=True)

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle put request by updating fire engines and return list of fire engines."""
        return self.update(request, *args, **kwargs)

    def update(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Update fire engines according to the id data and return list of fire engines."""
        fire_engine_id = request.data.get('id')
        instance = self.get_queryset().get(id=fire_engine_id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def __check_fire_engine_capacity(self, request, *args, **kwargs):
        """Check if number of fire engines exceed the capacity."""
        fire_station_id = request.data.get('station')
        fire_station = models.Station.objects.get(id=fire_station_id)
        if models.FireEngine.objects.filter(
                station_id=fire_station_id).count() >= fire_station.fire_engine_capacity:
            return response.Response({"message": "Exceed Fire Engine capacity."},
                                     status=status.HTTP_400_BAD_REQUEST)
