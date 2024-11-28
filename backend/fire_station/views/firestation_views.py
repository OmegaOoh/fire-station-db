from typing import Any
from rest_framework import decorators, response, generics, mixins
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
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
    
    def retrieve(self, request, *args, **kwargs):
        res = super().retrieve(request, *args, **kwargs)

        ff = self.get_object().staff_set.filter(firefighter__isnull=False)
        res.data['role_count'] = ff.values('firefighter__role').annotate(amount=Count('id'))
        res.data['rank_count'] = ff.values('firefighter__rank').annotate(amount=Count('id'))
        
        return res