"""Fire station model serializer"""
from rest_framework import serializers
from . import models

class EquipmentSerializer(serializers.ModelSerializer):
    """Equipment model serializer"""
    
    class Meta:
        model = models.Equipment
        fields = ('__all__')


class FireEngineSerializer(serializers.ModelSerializer):
    """Fire engine model serializer"""

    equipment_detail = EquipmentSerializer(source='equipments', many=True, read_only=True)
        
    class Meta:
        model = models.FireEngine
        fields = ('__all__')


class FireStationSerializer(serializers.ModelSerializer):
    """Fire station model serializer"""
    
    fire_engine = FireEngineSerializer(source='fireengine_set', many=True, read_only=True)

    class Meta:
        model = models.Station
        fields = ('__all__')
