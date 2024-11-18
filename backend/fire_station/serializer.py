"""Fire station model serializer"""
from rest_framework import serializers
from . import models


class FireStationSerializer(serializers.ModelSerializer):
    """Fire station model serializer"""

    class Meta:
        model = models.Station
        fields = ('__all__')


class Equipment(serializers.ModelSerializer):
    """Fire station model serializer"""

    class Meta:
        model = models.Station
        fields = ('__all__')
