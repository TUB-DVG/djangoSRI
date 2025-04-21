from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Import SRI models from the updated structure
from sridb.modules.sri.sri import (
    SRIAssessor,
    SRIBuilding,
    SRIMethodology,
    SRISriAssessment,
    SRIUsecase,
    SRIDomain,
    SRIServiceCatalogue,
    SRISriservice,
    SRIFunctionalitylevel
)

# Import Information Need models - keep if still needed
from sridb.modules.sri.information_need import (
    SRIAssetData, 
    SRIIndoorEnvironmentalData, 
    SRIControlLogic, 
    SRICyberDeviceData, 
    SRIDatacategoryMeta, 
    SRIEnergyData, 
    SRIOperationalData, 
    SRIOutdoorenvironmentalData, 
    SRIOnsiteenergygeneration
)

# Import ICT models - keep if still needed
from .modules.sri.ict import (
    SRIInformationNeed,
    SRISupportedAccess,
    SRIDataSource,
    SRIModel,
    SRIInterface,
    SRIDevice,
    SRIDataConnector
)

# Inline classes for the admin interface
class FunctionalityLevelInline(admin.TabularInline):
    model = SRIFunctionalitylevel
    extra = 1
    fields = ('functionalitylevel', 'description', 'name')

# Building Admin
@admin.register(SRIBuilding)
class SRIBuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'buildingstate', 'buildingusage', 'climatezone', 'sribuildingtype')
    list_filter = ('buildingstate', 'buildingusage', 'sribuildingtype', 'climatezone')
    search_fields = ('id__id', 'location', 'sridescription')
    fieldsets = (
        ('Building Information', {
            'fields': ('id', 'sridescription', 'location', 'usefulfloorarea')
        }),
        ('Classification', {
            'fields': ('buildingstate', 'buildingusage', 'sribuildingtype', 'climatezone')
        }),
    )

# Assessor Admin
@admin.register(SRIAssessor)
class SRIAssessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organisation', 'email', 'phonenumber')
    search_fields = ('name', 'organisation', 'email')

# Assessment Admin
@admin.register(SRISriAssessment)
class SRISriAssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dateofassessment', 'score', 'assessor_name')
    list_filter = ('dateofassessment', 'score')
    search_fields = ('id__id', 'assessor_assessments__name')
    
    def assessor_name(self, obj):
        return obj.assessor_assessments.name if obj.assessor_assessments else "-"
    assessor_name.short_description = 'Assessor'

# Methodology Admin
@admin.register(SRIMethodology)
class SRIMethodologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'preferredservicecatalogue', 'preferredweightings')
    search_fields = ('preferredservicecatalogue', 'preferredweightings')

# Use Case Admin
@admin.register(SRIUsecase)
class SRIUsecaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

# Domain Admin
@admin.register(SRIDomain)
class SRIDomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('category', 'description')

# Service Catalogue Admin
@admin.register(SRIServiceCatalogue)
class SRIServiceCatalogueAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'version', 'service_count')
    search_fields = ('description', 'version')
    
    def service_count(self, obj):
        count = obj.sri_services.count()
        return format_html('<a href="{}?catalogue__id={}">{} services</a>',
                         '/admin/sridb/srisriservice/',
                         obj.id,
                         count)
    service_count.short_description = 'Number of Services'

# SRI Service Admin
@admin.register(SRISriservice)
class SRISriserviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'domaintype_category', 'servicegroup', 'part_status')
    list_filter = ('domaintype_category', 'servicegroup')
    search_fields = ('code', 'name', 'domaintype_category', 'domaintype_description')
    inlines = [FunctionalityLevelInline]
    
    def part_status(self, obj):
        parts = []
        if obj.partofmethod:
            parts.append('Method A')
        if obj.partofmethodb:
            parts.append('Method B')
        return ', '.join(parts) if parts else 'None'
    part_status.short_description = 'Methods'

# Functionality Level Admin
@admin.register(SRIFunctionalitylevel)
class SRIFunctionalitylevelAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'functionalitylevel', 'description_preview')
    search_fields = ('sri_service__name', 'description', 'name')
    
    def service_name(self, obj):
        return obj.sri_service.name if obj.sri_service else "-"
    service_name.short_description = 'Service'
    
    def description_preview(self, obj):
        if not obj.description:
            return "-"
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_preview.short_description = 'Description'

# Keep the existing registrations for Information Need models if still needed
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
    list_display = ('id', 'datascale')
    list_filter = ('datascale',)
    search_fields = ('id__cityobject_id', 'datascale') # Assuming ObjectClass has a 'name' field

@admin.register(SRIEnergyData)
class SRIEnergyDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'enduse', 'energysource')
    list_filter = ('enduse', 'energysource')
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

@admin.register(SRIOnsiteenergygeneration)
class SRIOnsiteenergygenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'renewableenergy', 'nonrenewableenergy')
    list_filter = ('renewableenergy', 'nonrenewableenergy')
    search_fields = ('id__cityobject_id', 'renewableenergy', 'nonrenewableenergy')

# Register ICT models
@admin.register(SRIInformationNeed)
class SRIInformationNeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'objectclass')
    search_fields = ('id__id', 'description', 'objectclass__name') # Accessing CityObject and ObjectClass fields
    raw_id_fields = ('objectclass',)

@admin.register(SRISupportedAccess)
class SRISupportedAccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'hasapi', 'hasendpoint')
    search_fields = ('description',)

@admin.register(SRIDataSource)
class SRIDataSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'objectclass')
    search_fields = ('id__id', 'name', 'description', 'objectclass__name') # Accessing CityObject and ObjectClass fields
    raw_id_fields = ('objectclass',)

@admin.register(SRIModel)
class SRIModelAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id__id',) # Accessing SRIDataSource fields

@admin.register(SRIInterface)
class SRIInterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'supportedaccesst_description', 'supportedaccesst_hasendpoint', 'supportedaccesstype_hasapi')
    search_fields = ('id__id', 'supportedaccesst_description') # Accessing SRIDataSource fields

@admin.register(SRIDevice)
class SRIDeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'objectclass', 'supportedaccesst_description', 'supportedaccesst_hasendpoint', 'supportedaccesstype_hasapi')
    search_fields = ('id__id', 'manufacturer', 'objectclass__name', 'supportedaccesst_description') # Accessing SRIDataSource and ObjectClass fields
    raw_id_fields = ('objectclass',)

@admin.register(SRIDataConnector)
class SRIDataConnectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelschema', 'urlmodelschema')
    search_fields = ('id__id', 'modelschema', 'urlmodelschema') # Accessing CityObject fields
