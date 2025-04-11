from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sridb.views import (
    BuildingViewSet, SRIServiceViewSet, 
    assign_service_to_building, get_building_gml, get_available_services,
    SRIAssetDataViewSet, SRIIndoorEnvironmentalDataViewSet, SRIControlLogicViewSet, 
    SRICyberDeviceDataViewSet, SRIDatacategoryMetaViewSet, SRIEnergyDataViewSet, 
    SRIOperationalDataViewSet, SRIOutdoorenvironmentalDataViewSet, 
    SRIOnsiteenergygeneratioViewSet
)

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'services', SRIServiceViewSet)

# Register the new ViewSets
router.register(r'sri-asset-data', SRIAssetDataViewSet)
router.register(r'sri-indoor-environmental-data', SRIIndoorEnvironmentalDataViewSet)
router.register(r'sri-control-logic', SRIControlLogicViewSet)
router.register(r'sri-cyber-device-data', SRICyberDeviceDataViewSet)
router.register(r'sri-datacategory-meta', SRIDatacategoryMetaViewSet)
router.register(r'sri-energy-data', SRIEnergyDataViewSet)
router.register(r'sri-operational-data', SRIOperationalDataViewSet)
router.register(r'sri-outdoor-environmental-data', SRIOutdoorenvironmentalDataViewSet)
router.register(r'sri-onsite-energy-generation', SRIOnsiteenergygeneratioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('assign-service/<str:building_id>/<int:service_id>/', assign_service_to_building, name="assign_service"),
    path('building-gml/<str:building_id>/', get_building_gml, name="get_building_gml"),
    path('available-services/<int:sri_level_id>/', get_available_services, name="get_available_services"),

]
