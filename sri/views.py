from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sri.models import Building, Service
from sri.serializers import BuildingSerializer, ServiceSerializer
from sri.auxillary.gml_generator import generate_gml

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@api_view(['POST'])
def assign_service_to_building(request, building_id, service_id):
    """Assigns a Service to a Building"""
    building = get_object_or_404(Building, building_id=building_id)
    service = get_object_or_404(Service, id=service_id)
    building.services.add(service)
    return Response({"message": f"Service {service.name} assigned to Building {building_id}"})

@api_view(['GET'])
def get_building_gml(request, building_id):
    """API-View to Return CityGML Representation of a Building"""
    building = get_object_or_404(Building, building_id=building_id)
    pydantic_building = building.to_pydantic()
    gml_data = generate_gml(pydantic_building)

    response = HttpResponse(gml_data, content_type="application/xml")
    response['Content-Disposition'] = f'attachment; filename="{building_id}.gml"'
    return response

@api_view(['GET'])
def get_available_services(request, sri_level_id):
    """Returns all services available for a given SRI Level"""
    services = Service.objects.filter(sri_level_id=sri_level_id)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)
