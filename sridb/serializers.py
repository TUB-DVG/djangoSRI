from rest_framework import serializers
from sridb.modules.sri.sri import (
    SRIFunctionalitylevel, SRISriservice, SRIBuilding, SRISriAssessment,
    SRIServiceCatalogue, SRIMethodology, SRIAssessor, SRIDomain, SRIUsecase
)
from citydb.modules.bldg.building import Building
# Import the information need models
from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic, 
    SRICyberDeviceData, SRIDatacategoryMeta, SRIEnergyData, 
    SRIOperationalData, SRIOutdoorenvironmentalData, SRIOnsiteenergygeneration
)

"""
This file contains serializers for the SRI (Smart Readiness Indicator) models.
Serializers convert complex data types (like Django models) to Python data types
that can then be easily rendered into JSON, XML or other content types.
They also provide deserialization, allowing parsed data to be converted back
into complex types after validating the incoming data.
"""

class SRIServiceCatalogueSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Service Catalogue model."""
    class Meta:
        model = SRIServiceCatalogue
        fields = '__all__'

class SRIFunctionalityLevelSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Functionality Level model."""
    class Meta:
        model = SRIFunctionalitylevel
        fields = '__all__'

class SRIServiceSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Service model."""
    functionality_levels = SRIFunctionalityLevelSerializer(many=True, read_only=True)
    catalogue_details = SRIServiceCatalogueSerializer(source='catalogue', read_only=True)
    
    class Meta:
        model = SRISriservice
        fields = ['id', 'code', 'name', 'domain', 'impact', 'servicegroup', 
                  'partofmethod', 'partofmethodb', 'preconditions', 'userdefined',
                  'catalogue', 'catalogue_details', 'functionality_levels']

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
        fields = ['id', 'building', 'buildingstate', 'buildingusage', 'climatezone', 
                  'location', 'sribuildingtype', 'usefulfloorarea', 'sri_description']

class SRIAssessorSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Assessor model."""
    class Meta:
        model = SRIAssessor
        fields = '__all__'

class SRIMethodologySerializer(serializers.ModelSerializer):
    """Serializer for the SRI Methodology model."""
    class Meta:
        model = SRIMethodology
        fields = '__all__'

class SRIAssessmentSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Assessment model with related services."""
    services = SRIServiceSerializer(source='sri_services', many=True, read_only=True)
    buildings = SRIBuildingSerializer(many=True, read_only=True)
    assessor = SRIAssessorSerializer(source='assessor_assessments', read_only=True)
    methodology = SRIMethodologySerializer(source='methodology_assessments', read_only=True)
    
    class Meta:
        model = SRISriAssessment
        fields = ['id', 'dateofassessment', 'score', 'services', 
                  'buildings',
                  'assessor_assessments', 'assessor',
                  'methodology_assessments', 'methodology']

class SRIDomainSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Domain model."""
    class Meta:
        model = SRIDomain
        fields = '__all__'

class SRIUsecaseSerializer(serializers.ModelSerializer):
    """Serializer for the SRI Usecase model."""
    class Meta:
        model = SRIUsecase
        fields = '__all__'

# Information Need model serializers
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

class SRIOnsiteenergygenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SRIOnsiteenergygeneration
        fields = '__all__'
