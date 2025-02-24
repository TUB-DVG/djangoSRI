from rest_framework import serializers
from .models import Building, Assessment, EnergySystem

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
