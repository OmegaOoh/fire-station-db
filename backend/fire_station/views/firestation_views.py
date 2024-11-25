from typing import Any
from rest_framework import decorators, response, generics, mixins
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .. import serializer
from .. import models


class FireStationView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):

    queryset = models.Station.objects.all()
    serializer_class = serializer.FireStationSerializer

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.create(request, args, kwargs)


class FireStationDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
):

    queryset = models.Station.objects.all()
    serializer_class = serializer.FireStationSerializer

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.retrieve(request, *args, **kwargs)
