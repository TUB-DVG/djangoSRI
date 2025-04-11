from django.contrib import admin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from sridb.models import SRILevel, Service, Building, BuildingPart, Assessor, Assessment, AssessmentMethod, EnergySystem, ServiceCatalog, ServiceGroup, ServiceDefinition, FunctionalityLevelDefinition, ServiceImplementation
# Import the new models
from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic, 
    SRICyberDeviceData, SRIDatacategoryMeta, SRIEnergyData, 
    SRIOperationalData, SRIOutdoorenvironmentalData, SRIOnsiteenergygeneratio
)

from django.utils.html import format_html

# Inline Models for Better Admin UI
class ServiceInline(admin.TabularInline):
    model = Building.services.through
    extra = 1  

class AssessmentInline(admin.TabularInline):
    model = Building.assessments.through
    extra = 1

class EnergySystemInline(admin.TabularInline):
    model = Building.energy_systems.through
    extra = 1

# Bulk Actions for Buildings
@admin.action(description="Assign selected Services to Buildings")
def assign_services_to_buildings(modeladmin, request, queryset):
    """Assigns a predefined set of services to multiple selected buildings"""
    service_ids = request.POST.getlist('_selected_action')  # Get selected services from admin UI
    services = Service.objects.filter(id__in=service_ids)

    for building in queryset:
        building.services.add(*services)

    modeladmin.message_user(request, f"{len(services)} services assigned to {len(queryset)} buildings.")

@admin.action(description="Change SRI Level for selected Buildings")
def change_sri_level(modeladmin, request, queryset):
    """Change the SRI Level for selected buildings"""
    sri_level_id = request.POST.get('sri_level')  # Get selected SRI Level
    sri_level = SRILevel.objects.get(id=sri_level_id)

    queryset.update(sri_level=sri_level)
    modeladmin.message_user(request, f"SRI Level updated to {sri_level.level_name} for {len(queryset)} buildings.")

# Bulk Actions for Building Parts
@admin.action(description="Assign selected Services to Building Parts")
def assign_services_to_building_parts(modeladmin, request, queryset):
    """Assigns a predefined set of services to multiple selected building parts"""
    service_ids = request.POST.getlist('_selected_action')
    services = Service.objects.filter(id__in=service_ids)

    for building_part in queryset:
        building_part.services.add(*services)

    modeladmin.message_user(request, f"{len(services)} services assigned to {len(queryset)} building parts.")

@admin.register(SRILevel)
class SRILevelAdmin(admin.ModelAdmin):
    list_display = ("level_name", "level_value", "valid_for_building_part")
    list_filter = ("valid_for_building_part",)
    search_fields = ("level_name",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "technical_domain", "desired_impact", "sri_level")
    list_filter = ("technical_domain", "desired_impact", "sri_level")
    search_fields = ("name",)

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("building_id", "sri_level")
    list_filter = ("sri_level",)
    search_fields = ("building_id",)
    inlines = [ServiceInline, AssessmentInline, EnergySystemInline]
    actions = [assign_services_to_buildings, change_sri_level]  # Add bulk actions

@admin.register(BuildingPart)
class BuildingPartAdmin(admin.ModelAdmin):
    list_display = ("building_id", "parent_building", "sri_level")
    list_filter = ("sri_level",)
    search_fields = ("building_id", "parent_building__building_id")
    actions = [assign_services_to_building_parts]  # Add bulk actions

@admin.register(Assessor)
class AssessorAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "certification_id")
    search_fields = ("name", "organization")

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("category", "score", "assessor")
    list_filter = ("category", "score")
    search_fields = ("category", "assessor__name")

@admin.register(AssessmentMethod)
class AssessmentMethodAdmin(admin.ModelAdmin):
    list_display = ("method_type", "description")
    search_fields = ("method_type",)

@admin.register(EnergySystem)
class EnergySystemAdmin(admin.ModelAdmin):
    list_display = ("system_type", "efficiency_score")
    list_filter = ("system_type",)
    search_fields = ("system_type",)

class FunctionalityLevelInline(admin.TabularInline):
    model = FunctionalityLevelDefinition
    extra = 1
    fields = ('level', 'description', 'is_non_smart_default')
    ordering = ('level',)

@admin.register(ServiceCatalog)
class ServiceCatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'publication_date', 'is_active', 'service_count')
    list_filter = ('is_active', 'publication_date')
    search_fields = ('name', 'version', 'description')
    
    def service_count(self, obj):
        count = obj.services.count()
        return format_html('<a href="{}?catalog__id={}">{} services</a>',
                         '/admin/sri/servicedefinition/',
                         obj.id,
                         count)
    service_count.short_description = 'Number of Services'

@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'technical_domain', 'service_count')
    list_filter = ('technical_domain',)
    search_fields = ('name', 'code')
    ordering = ('technical_domain', 'code')

    def service_count(self, obj):
        return obj.services.count()
    service_count.short_description = 'Number of Services'

@admin.register(ServiceDefinition)
class ServiceDefinitionAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'name', 'technical_domain', 'service_group', 
                   'triage_score', 'part_status', 'is_applicable')
    list_filter = ('technical_domain', 'service_group', 'desired_impact', 
                  'is_applicable', 'part_a', 'part_b', 'part_c')
    search_fields = ('service_id', 'name', 'description')
    inlines = [FunctionalityLevelInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('catalog', 'service_id', 'name', 'description')
        }),
        ('Classification', {
            'fields': ('technical_domain', 'service_group', 'desired_impact')
        }),
        ('Requirements', {
            'fields': ('is_applicable', 'preconditions', 'triage_score')
        }),
        ('Part Status', {
            'fields': ('part_a', 'part_b', 'part_c')
        }),
    )

    def part_status(self, obj):
        parts = []
        if obj.part_a:
            parts.append('A')
        if obj.part_b:
            parts.append('B')
        if obj.part_c:
            parts.append('C')
        return ', '.join(parts) if parts else 'None'
    part_status.short_description = 'Parts'

@admin.register(FunctionalityLevelDefinition)
class FunctionalityLevelDefinitionAdmin(admin.ModelAdmin):
    list_display = ('service_definition', 'level', 'description_preview', 'is_non_smart_default')
    list_filter = ('is_non_smart_default', 'service_definition__technical_domain')
    search_fields = ('service_definition__name', 'description')
    ordering = ('service_definition', 'level')

    def description_preview(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_preview.short_description = 'Description'

@admin.register(ServiceImplementation)
class ServiceImplementationAdmin(admin.ModelAdmin):
    list_display = ('building', 'service_definition', 'current_functionality_level', 
                   'implementation_date', 'is_active')
    list_filter = ('is_active', 'implementation_date', 
                  'service_definition__technical_domain')
    search_fields = ('building__building_id', 'service_definition__name', 'notes')
    date_hierarchy = 'implementation_date'
    raw_id_fields = ('building', 'service_definition', 'current_functionality_level')

    fieldsets = (
        ('Implementation Details', {
            'fields': ('building', 'service_definition', 'current_functionality_level')
        }),
        ('Status', {
            'fields': ('is_active', 'notes')
        }),
        ('Timestamps', {
            'fields': ('implementation_date', 'last_updated'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('implementation_date', 'last_updated')

# Register the new models
@admin.register(SRIAssetData)
class SRIAssetDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'assettype', 'other')
    list_filter = ('assettype',)
    search_fields = ('id__cityobject_id', 'other')  # Assuming CityObject has a field like cityobject_id

@admin.register(SRIIndoorEnvironmentalData)
class SRIIndoorEnvironmentalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'environmentaldatatype', 'other')
    list_filter = ('environmentaldatatype',)
    search_fields = ('id__cityobject_id', 'other')

@admin.register(SRIControlLogic)
class SRIControlLogicAdmin(admin.ModelAdmin):
    list_display = ('id', 'controlsystem', 'controltype')
    list_filter = ('controlsystem', 'controltype')
    search_fields = ('id__id', 'id__description') # Accessing SRIDatacategorymeta fields

@admin.register(SRICyberDeviceData)
class SRICyberDeviceDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'cyberdevicetype', 'other')
    list_filter = ('cyberdevicetype',)
    search_fields = ('id__cityobject_id', 'other')

@admin.register(SRIDatacategoryMeta)
class SRIDatacategoryMetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'datascale', 'description', 'designtype', 'objectclass', 'occupanttype', 'utilitygridtype')
    list_filter = ('datascale', 'designtype', 'objectclass', 'occupanttype', 'utilitygridtype')
    search_fields = ('id__cityobject_id', 'description', 'objectclass__name') # Assuming ObjectClass has a 'name' field
    raw_id_fields = ('objectclass',) # For better handling of ForeignKey

@admin.register(SRIEnergyData)
class SRIEnergyDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'enduse', 'energysource', 'scale')
    list_filter = ('enduse', 'energysource', 'scale')
    search_fields = ('id__id', 'id__description') # Accessing SRIDatacategorymeta fields

@admin.register(SRIOperationalData)
class SRIOperationalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'systemdata', 'systemtype')
    list_filter = ('systemdata', 'systemtype')
    search_fields = ('id__id', 'id__description') # Accessing SRIDatacategorymeta fields

@admin.register(SRIOutdoorenvironmentalData)
class SRIOutdoorenvironmentalDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'environmentaldatatype', 'other', 'source')
    list_filter = ('environmentaldatatype', 'source')
    search_fields = ('id__cityobject_id', 'other', 'source')

@admin.register(SRIOnsiteenergygeneratio)
class SRIOnsiteenergygeneratioAdmin(admin.ModelAdmin):
    list_display = ('id', 'renewableenergy', 'nonrenewableenergy')
    list_filter = ('renewableenergy', 'nonrenewableenergy')
    search_fields = ('id__cityobject_id', 'renewableenergy', 'nonrenewableenergy')
