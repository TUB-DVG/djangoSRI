from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sridb.views import BuildingViewSet, SRIServiceViewSet, assign_service_to_building, get_building_gml, get_available_services

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet)
router.register(r'services', SRIServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('assign-service/<str:building_id>/<int:service_id>/', assign_service_to_building, name="assign_service"),
    path('building-gml/<str:building_id>/', get_building_gml, name="get_building_gml"),
    path('available-services/<int:sri_level_id>/', get_available_services, name="get_available_services"),

]
