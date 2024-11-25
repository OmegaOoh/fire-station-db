from typing import Any
from rest_framework import response, generics, mixins
from django.http import HttpRequest
from .serializers import ShiftSerializer
from .models import Shift

class ShiftView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Shift.objects.all() 
    serializer_class = ShiftSerializer 

    #Handle request to get shift
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.list(request, *args, **kwargs)

    #Handle request to create new shift
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.create(request, *args, **kwargs)
        
    #Handle request to change entrie shift
    def put(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.update(request, *args, **kwargs)
        
    #Handle request to update specific info
    def patch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.partial_update(request, *args, **kwargs)

    #Handle request to delete shift
    def delete(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.destroy(request, *args, **kwargs)
