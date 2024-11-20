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


class FireFighterSerializer(serializers.ModelSerializer):
    """Fire fighter model serializer"""

    class Meta:
        model = models.FireFighter
        fields = ('__all__')


class StaffSerializer(serializers.ModelSerializer):
    """Staff model serializer"""

    fire_fighter = FireFighterSerializer(source='firefighter')

    class Meta:
        model = models.Staff
        fields = ('__all__')
