from rest_framework import serializers
from sri.models import Building, BuildingPart, Service, SRILevel

class SRILevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRILevel
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    sri_level = SRILevelSerializer()

    class Meta:
        model = Service
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = Building
        fields = '__all__'

class BuildingPartSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    parent_building = BuildingSerializer()

    class Meta:
        model = BuildingPart
        fields = '__all__'
