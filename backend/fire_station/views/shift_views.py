from typing import Any
from rest_framework import response, generics, mixins
from django.http import HttpRequest
from ..serializer import ShiftSerializer
from ..models import Shift

#Handle showing list
class ShiftView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Shift.objects.all() 
    serializer_class = ShiftSerializer 

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.create(request, *args, **kwargs)

#Handle changing information
class ShiftChangeView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Shift.objects.all() 
    serializer_class = ShiftSerializer 

    def put(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        return self.destroy(request, *args, **kwargs)