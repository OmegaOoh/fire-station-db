"""Fire station model serializer"""
from rest_framework import serializers
from . import models


class EquipmentSerializer(serializers.ModelSerializer):
    """Equipment model serializer"""
    
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Equipment
        fields = ('__all__')

    def get_selected(self, obj):
        return False

class FireEngineSerializer(serializers.ModelSerializer):
    """Fire engine model serializer"""

    equipment_detail = EquipmentSerializer(source='equipments', many=True, read_only=True)
    selected = serializers.SerializerMethodField()
        
    class Meta:
        model = models.FireEngine
        fields = ('__all__')
    
    def get_selected(self, obj):
        return False


class FireFighterSerializer(serializers.ModelSerializer):
    """Fire fighter model serializer"""

    class Meta:
        model = models.FireFighter
        fields = ('__all__')


class StaffSerializer(serializers.ModelSerializer):
    """Staff model serializer"""

    is_fire_fighter = serializers.BooleanField(required=False)
    firefighter_detail = FireFighterSerializer(source="firefighter", read_only=True)
    firefighter = serializers.DictField(write_only=True, default=None)
    station_name = serializers.StringRelatedField(source="station", read_only=True)
    selected = serializers.SerializerMethodField()

    class Meta:
        model = models.Staff
        fields = ('__all__')

    def create(self, validated_data):

        ff = validated_data.pop('firefighter', None)
        print(validated_data)
        print(ff)
        staff = super().create(validated_data)

        if ff:
            ff['staff'] = staff.id
            ff_serializer = FireFighterSerializer(data=ff)
            ff_serializer.is_valid(raise_exception=True)
            ff_serializer.save()

        return staff
    
    def get_selected(self, obj):
        return False


class FireStationSerializer(serializers.ModelSerializer):
    """Fire station model serializer"""

    fire_engine = FireEngineSerializer(source='fireengine_set', many=True, read_only=True)
    staff = StaffSerializer(source='staff_set', many=True, read_only=True)

    class Meta:
        model = models.Station
        fields = ('__all__')


class DispatchSerializer(serializers.ModelSerializer):
    """Dispatch model serializer"""

    class Meta:
        model = models.Dispatch
        fields = ('__all__')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['incident'] = instance.incident.label
        ret['station'] = instance.station.station_name
        return ret

        
class ShiftSerializer(serializers.ModelSerializer):
    """Fire station model serializer"""
    
    class Meta:
        model = models.Shift
        fields = ('__all__')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['day'] = instance.day.label
        return ret