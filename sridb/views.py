from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from citydb.modules.energy.core.energybuilding import EnergyBuilding
from citydb.modules.bldg.building import Building
from sridb.modules.sri.sri import SRISriservice, SRIBuilding, SRISriassessment
from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic, 
    SRICyberDeviceData, SRIDatacategoryMeta, SRIEnergyData, 
    SRIOperationalData, SRIOutdoorenvironmentalData, SRIOnsiteenergygeneratio
)
from sridb.serializers import (
    BuildingSerializer, SRIServiceSerializer, SRIBuildingSerializer, 
    SRIAssessmentSerializer, SRIAssetDataSerializer,
    SRIIndoorEnvironmentalDataSerializer, SRIControlLogicSerializer, 
    SRICyberDeviceDataSerializer, SRIDatacategoryMetaSerializer, 
    SRIEnergyDataSerializer, SRIOperationalDataSerializer, 
    SRIOutdoorenvironmentalDataSerializer, SRIOnsiteenergygeneratioSerializer
)
from sridb.auxillary.gml_generator import generate_gml

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SRIServiceViewSet(viewsets.ModelViewSet):
    queryset = SRISriservice.objects.all()
    serializer_class = SRIServiceSerializer

@api_view(['POST'])
def assign_service_to_building(request, building_id, service_id):
    """Assigns a SRI Service to a Building"""
    building = get_object_or_404(SRIBuilding, id=building_id)
    service = get_object_or_404(SRISriservice, id=service_id)
    building.services.add(service)
    return Response({"message": f"Service {service.name} assigned to Building {building_id}"})

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
def get_available_services(request, sri_level_id):
    """Returns all services available for a given SRI Level"""
    services = SRISriservice.objects.filter(sri_level_id=sri_level_id)
    serializer = SRIServiceSerializer(services, many=True)
    return Response(serializer.data)

# ViewSets for the new Information Need models

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

class SRIOnsiteenergygeneratioViewSet(viewsets.ModelViewSet):
    queryset = SRIOnsiteenergygeneratio.objects.all()
    serializer_class = SRIOnsiteenergygeneratioSerializer
