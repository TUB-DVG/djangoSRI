from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from citydb.modules.energy.core.energybuilding import EnergyBuilding
from citydb.modules.bldg.building import Building
from sridb.modules.sri.sri import (
    SRISriservice, SRIBuilding, SRISriAssessment, 
    SRIServiceCatalogue, SRIMethodology,
    SRIAssessor 
)
from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic, 
    SRICyberDeviceData, SRIDatacategoryMeta, SRIEnergyData, 
    SRIOperationalData, SRIOutdoorenvironmentalData,
     SRIOnsiteenergygeneration, SRIUsecase
)
from sridb.serializers import (
    BuildingSerializer, SRIServiceSerializer, SRIBuildingSerializer, 
    SRIAssessmentSerializer, SRIAssetDataSerializer,
    SRIIndoorEnvironmentalDataSerializer, SRIControlLogicSerializer, 
    SRICyberDeviceDataSerializer, SRIDatacategoryMetaSerializer, 
    SRIEnergyDataSerializer, SRIOperationalDataSerializer, 
    SRIOutdoorenvironmentalDataSerializer, SRIOnsiteenergygenerationSerializer,
    SRIMethodologySerializer, SRIAssessorSerializer, 
      SRIUsecaseSerializer, SRIServiceCatalogueSerializer
)
from sridb.auxillary.gml_generator import generate_gml

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SRIBuildingViewSet(viewsets.ModelViewSet):
    queryset = SRIBuilding.objects.all()
    serializer_class = SRIBuildingSerializer

class SRIServiceViewSet(viewsets.ModelViewSet):
    queryset = SRISriservice.objects.all()
    serializer_class = SRIServiceSerializer

class SRIAssessmentViewSet(viewsets.ModelViewSet):
    queryset = SRISriAssessment.objects.all()
    serializer_class = SRIAssessmentSerializer

class SRIMethodologyViewSet(viewsets.ModelViewSet):
    queryset = SRIMethodology.objects.all()
    serializer_class = SRIMethodologySerializer

class SRIAssessorViewSet(viewsets.ModelViewSet):
    queryset = SRIAssessor.objects.all()
    serializer_class = SRIAssessorSerializer


class SRIUsecaseViewSet(viewsets.ModelViewSet):
    queryset = SRIUsecase.objects.all()
    serializer_class = SRIUsecaseSerializer

class SRIServiceCatalogueViewSet(viewsets.ModelViewSet):
    queryset = SRIServiceCatalogue.objects.all()
    serializer_class = SRIServiceCatalogueSerializer

@api_view(['POST'])
def assign_service_to_building(request, building_id, service_id):
    """Assigns a SRI Service to a Building via an Assessment"""
    building = get_object_or_404(SRIBuilding, id=building_id)
    service = get_object_or_404(SRISriservice, id=service_id)
    
    # With the new model structure, we need to assign services through assessments
    # Check if the building has an assessment, create one if not
    # First try to get from the direct relationship
    assessment = None
    
    # Look for existing assessments linked to this building
    existing_assessments = building.assessments.all()
    if existing_assessments.exists():
        # Use the first assessment if there's already one
        assessment = existing_assessments.first()
    
    if assessment is None:
        # Create a new assessment and link it to the building
        assessment = SRISriAssessment.objects.create(
            score=0  # Default score value
        )
        # Link using the M2M relationship
        assessment.buildings.add(building)
        assessment.save()
    
    # Add the service to the assessment
    assessment.sri_services.add(service)
    
    return Response({
        "message": f"Service {service.name} assigned to Building {building_id} via Assessment {assessment.id}",
        "assessment_id": assessment.id
    })

@api_view(['GET'])
def get_building_gml(request, building_id):
    """API-View to Return CityGML Representation of a Building"""
    building = get_object_or_404(Building, id=building_id)
    pydantic_building = building.to_pydantic()
    gml_data = generate_gml(pydantic_building)

    response = HttpResponse(gml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename="{building_id}.gml"'
    return response

@api_view(['GET'])
def get_available_services(request, catalogue_id=None):
    """Returns all services available for a given SRI Catalogue"""
    if catalogue_id:
        services = SRISriservice.objects.filter(catalogue_id=catalogue_id)
    else:
        services = SRISriservice.objects.all()
    
    serializer = SRIServiceSerializer(services, many=True)
    return Response(serializer.data)

# ViewSets for the Information Need models
class SRIAssetDataViewSet(viewsets.ModelViewSet):
    queryset = SRIAssetData.objects.all()
    serializer_class = SRIAssetDataSerializer

class SRIIndoorEnvironmentalDataViewSet(viewsets.ModelViewSet):
    queryset = SRIIndoorEnvironmentalData.objects.all()
    serializer_class = SRIIndoorEnvironmentalDataSerializer

class SRIControlLogicViewSet(viewsets.ModelViewSet):
    queryset = SRIControlLogic.objects.all()
    serializer_class = SRIControlLogicSerializer

class SRICyberDeviceDataViewSet(viewsets.ModelViewSet):
    queryset = SRICyberDeviceData.objects.all()
    serializer_class = SRICyberDeviceDataSerializer

class SRIDatacategoryMetaViewSet(viewsets.ModelViewSet):
    queryset = SRIDatacategoryMeta.objects.all()
    serializer_class = SRIDatacategoryMetaSerializer

class SRIEnergyDataViewSet(viewsets.ModelViewSet):
    queryset = SRIEnergyData.objects.all()
    serializer_class = SRIEnergyDataSerializer

class SRIOperationalDataViewSet(viewsets.ModelViewSet):
    queryset = SRIOperationalData.objects.all()
    serializer_class = SRIOperationalDataSerializer

class SRIOutdoorenvironmentalDataViewSet(viewsets.ModelViewSet):
    queryset = SRIOutdoorenvironmentalData.objects.all()
    serializer_class = SRIOutdoorenvironmentalDataSerializer

class SRIOnsiteenergygenerationViewSet(viewsets.ModelViewSet):
    queryset = SRIOnsiteenergygeneration.objects.all()
    serializer_class = SRIOnsiteenergygenerationSerializer
