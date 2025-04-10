from rest_framework import serializers
from sridb.modules.sri.sri import SRIFunctionalitylevel, SRISriservice, SRIBuilding, SRISriassessment
from citydb.modules.bldg.building import Building

"""
This file contains serializers for the SRI (Smart Readiness Indicator) models.
Serializers convert complex data types (like Django models) to Python data types
that can then be easily rendered into JSON, XML or other content types.
They also provide deserialization, allowing parsed data to be converted back
into complex types after validating the incoming data.
"""

class SRIFunctionalityLevelSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Functionality Level model."""
    class Meta:
        model = SRIFunctionalitylevel
        fields = '__all__'

class SRIServiceSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Service model."""
    class Meta:
        model = SRISriservice
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    """Serializer for the Building model."""
    class Meta:
        model = Building
        fields = '__all__'

class SRIBuildingSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Building model with related building data."""
    building = BuildingSerializer(source='id', read_only=True)
    
    class Meta:
        model = SRIBuilding
        fields = ['building', 'buildingstate', 'buildingusage', 'climatezone', 
                  'location', 'sribuildingtype', 'usefulfloorarea']

class SRIAssessmentSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Assessment model with related services."""
    services = SRIServiceSerializer(source='sri_services', many=True, read_only=True)
    
    class Meta:
        model = SRISriassessment
        fields = ['id', 'dateofassessment', 'fullbuilding', 'score', 'services']
