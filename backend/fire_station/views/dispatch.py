"""Module for handle dispatch."""
from typing import Any
from django.http import HttpRequest
from django.db.models import QuerySet
from rest_framework import generics, mixins, response, status
from fire_station import models, serializer


class DispatchView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """Return list of dispatches when GET request and create new dispatches when POST request."""

    serializer_class = serializer.DispatchSerializer

    def get_queryset(self) -> QuerySet:
        """Equipments view return list of all dispatches."""
        return models.Dispatch.objects.all()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by return with list of equipments.

        :param request: Http request object
        :return: Http response object
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle post request by creating dispatches and return list of dispatches.

        :param request: Http request object
        :return: Http response object
        """
        self.create(request, *args, **kwargs)

        serializer = self.get_serializer(self.get_queryset(), many=True)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
