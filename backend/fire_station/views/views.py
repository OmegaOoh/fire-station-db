from rest_framework import decorators, response
from django.http import HttpRequest


@decorators.api_view(['GET'])
def test_view(request: HttpRequest) -> response.Response:
    return response.Response({'message': 'rest work ig'})
