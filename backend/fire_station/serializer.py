"""Fire station model serializer"""
from rest_framework import serializers
from . import models


class FireStationSerializer(serializers.ModelSerializer):
    """Fire station model serializer"""
    
    class Meta:
        model = models.Station
        fields = ('__all__')


class EquipmentSerializer(serializers.ModelSerializer):
    """Equipment model serializer"""
    
    class Meta:
        model = models.Equipment
        fields = ('__all__')


class FireEngineSerializer(serializers.ModelSerializer):
    """Fire engine model serializer"""

    class Meta:
        model = models.FireEngine
        fields = ('__all__')
