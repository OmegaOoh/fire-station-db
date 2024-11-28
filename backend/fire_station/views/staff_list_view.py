from typing import Any
from rest_framework import generics, mixins
from django.http import request, response
from django.views.decorators.csrf import csrf_exempt
from .. import models, serializer


class StaffList(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    queryset = models.Staff.objects.all()
    serializer_class = serializer.StaffSerializer

    def get(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponse:
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponse:
        return self.create(request, *args, **kwargs)

class StaffDetail(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin
):
    queryset = models.Staff.objects.all()
    serializer_class = serializer.StaffSerializer
    
    def get(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponse:
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request: request.HttpRequest, *args: Any, **kwargs: Any) -> response.HttpResponse:
        return self.update(request, partial=True ,*args, **kwargs)