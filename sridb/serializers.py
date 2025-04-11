from rest_framework import serializers
from sridb.modules.sri.sri import SRIFunctionalitylevel, SRISriservice, SRIBuilding, SRISriassessment
from citydb.modules.bldg.building import Building
# Import the new models
from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic, 
    SRICyberDeviceData, SRIDatacategoryMeta, SRIEnergyData, 
    SRIOperationalData, SRIOutdoorenvironmentalData, SRIOnsiteenergygeneratio
)

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

class SRIAssetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIAssetData
        fields = '__all__'

class SRIIndoorEnvironmentalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIIndoorEnvironmentalData
        fields = '__all__'

class SRIControlLogicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIControlLogic
        fields = '__all__'

class SRICyberDeviceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRICyberDeviceData
        fields = '__all__'

class SRIDatacategoryMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIDatacategoryMeta
        fields = '__all__'

class SRIEnergyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIEnergyData
        fields = '__all__'

class SRIOperationalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIOperationalData
        fields = '__all__'

class SRIOutdoorenvironmentalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIOutdoorenvironmentalData
        fields = '__all__'

class SRIOnsiteenergygeneratioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIOnsiteenergygeneratio
        fields = '__all__'
