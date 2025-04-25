from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, format_html_join
from django.urls import reverse

# Import SRI models from the updated structure
from sridb.modules.sri.sri import (
    SRIAssessor,
    SRIBuilding,
    SRIMethodology,
    SRISriAssessment,

    SRIServiceCatalogue,
    SRISriservice
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
    SRIOnsiteenergygeneration,
    SRIUsecase,
    SRIInformationNeed,
    SRIUtilityGridData
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



@admin.register(SRIBuilding)
class SRIBuildingAdmin(admin.ModelAdmin):
    list_display  = (
        'id',
        'buildingstate',
        'buildingusage',
        'climatezone',
        'sribuildingtype',
    )
    list_filter   = (
        'buildingstate',
        'buildingusage',
        'sribuildingtype',
        'climatezone',
    )
    search_fields = ('id__id', 'location', 'sridescription')

    fieldsets = (
        ('Building Information', {
            'fields': ('id', 'sridescription', 'location', 'usefulfloorarea')
        }),
        ('Classification', {
            'fields': ('buildingstate', 'buildingusage', 'sribuildingtype', 'climatezone')
        }),
    )
    
    # Add inline for services
    class SRIServiceInline(admin.TabularInline):
        model = SRISriservice
        extra = 1
        fields = ('code', 'servicename', 'sridomain', 'servicegroup', 'functionalitylevel', 'sharefunctionalitylevel')
        readonly_fields = ('code', 'servicename', 'sridomain', 'servicegroup', 'functionalitylevel', 'sharefunctionalitylevel')
        can_delete = False
        verbose_name = "Service"
        verbose_name_plural = "Building Services Inline"
    
    inlines = [SRIServiceInline]

    def get_queryset(self, request):
        # Prefetch all related SRISriservice objects in one go
        qs = super().get_queryset(request)
        return qs.prefetch_related('services')
    
    class SRIInformationNeedInline(admin.TabularInline):
        model = SRIInformationNeed
        extra = 1
        fields = ('id', 'descriptioninformationneed', 'objectclass')
        readonly_fields = ('id', 'descriptioninformationneed', 'objectclass')
        can_delete = False
        verbose_name = "Information Need"

    

# Assessor Admin
@admin.register(SRIAssessor)
class SRIAssessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organisation', 'email', 'phonenumber')
    search_fields = ('name', 'organisation', 'email')

# Assessment Admin
@admin.register(SRISriAssessment)
class SRISriAssessmentAdmin(admin.ModelAdmin):
    list_display = ('dateofassessment', 'score', 'assessor_name')
    list_filter = ('dateofassessment', 'score')
    #search_fields = ('assessor_id__name')
    #filter_horizontal = ('services',)
    
    def assessor_name(self, obj):
        return obj.assessor_id.name if obj.assessor_id else "-"
    assessor_name.short_description = 'Assessor'

# Methodology Admin
@admin.register(SRIMethodology)
class SRIMethodologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'preferredservicecatalogue', 'preferredweightings')
    search_fields = ('preferredservicecatalogue', 'preferredweightings')


# Service Catalogue Admin
@admin.register(SRIServiceCatalogue)
class SRIServiceCatalogueAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'version', 'service_count')
    search_fields = ('description', 'version')
    raw_id_fields = ('id',)
    
    def service_count(self, obj):
        count = obj.sri_services.count()
        return format_html('<a href="{}?catalogue__id={}">{} services</a>',
                         '/admin/sridb/srisriservice/',
                         obj.id.id if obj.id else '',
                         count)
    service_count.short_description = 'Number of Services'

# SRI Service Admin
@admin.register(SRISriservice)
class SRISriserviceAdmin(admin.ModelAdmin):
    list_display = ('code', 'servicename', 'sridomain', 'servicegroup', 'part_status')
    list_filter = ('sridomain', 'servicegroup', 'building')
    search_fields = ('code', 'servicename', 'sridomain', 'descriptionfunctionalityleve')
    raw_id_fields = ('catalogue', 'building') 
    fieldsets = (
        ('Basic Information', {
            'fields': ('code', 'servicename', 'sridomain', 'servicegroup')
        }),
        ('Relationships', {
            'fields': ('catalogue', 'building')
        }),
        ('Functionality', {
            'fields': ('functionalitylevel', 'descriptionfunctionalityleve', 'sharefunctionalitylevel')
        }),
        ('Method Settings', {
            'fields': ('_partofmethoda', '_partofmethodb', '_userdefined', 'preconditions')
        }),
    )
    
    class SRIInformationNeedInline(admin.TabularInline):
        model = SRIInformationNeed
        extra = 1
        fields = ('id', 'descriptioninformationneed', 'objectclass')
        readonly_fields = ('id', 'descriptioninformationneed', 'objectclass')
        can_delete = False
        verbose_name = "Information Need"
    
    inlines = [SRIInformationNeedInline]
    
    def part_status(self, obj):
        parts = []
        if obj.partofmethoda:
            parts.append('Method A')
        if obj.partofmethodb:
            parts.append('Method B')
        return ', '.join(parts) if parts else 'None'
    part_status.short_description = 'Methods'

@admin.register(SRIAssetData)
class SRIAssetDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'assettype', 'other')
    list_filter    = ('assettype',)
    search_fields  = ('id__id', 'other')


@admin.register(SRIIndoorEnvironmentalData)
class SRIIndoorEnvironmentalDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'environmentaldatatype', 'other')
    list_filter    = ('environmentaldatatype',)
    search_fields  = ('id__id', 'other')


@admin.register(SRIOutdoorenvironmentalData)
class SRIOutdoorenvironmentalDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'environmentaldatatype', 'source', 'other')
    list_filter    = ('environmentaldatatype', 'source')
    search_fields  = ('id__id', 'source', 'other')


@admin.register(SRIControlLogic)
class SRIControlLogicAdmin(admin.ModelAdmin):
    list_display   = ('id', 'controlsystem', 'controltype', 'datascale', 'other')
    list_filter    = ('controlsystem', 'controltype', 'datascale')
    search_fields  = ('id__id', 'other')


@admin.register(SRICyberDeviceData)
class SRICyberDeviceDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'cyberdevicetype', 'other')
    list_filter    = ('cyberdevicetype',)
    search_fields  = ('id__id', 'other')


@admin.register(SRIDatacategoryMeta)
class SRIDatacategoryMetaAdmin(admin.ModelAdmin):
    list_display   = ('id', 'datascale', 'other')
    list_filter    = ('datascale',)
    search_fields  = ('id__id', 'other')


@admin.register(SRIEnergyData)
class SRIEnergyDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'enduse', 'energysource')
    list_filter    = ('enduse', 'energysource')
    search_fields  = ('id__id',)


@admin.register(SRIOperationalData)
class SRIOperationalDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'systemdata', 'systemtype', 'other')
    list_filter    = ('systemdata', 'systemtype')
    search_fields  = ('id__id', 'other')


@admin.register(SRIUtilityGridData)
class SRIUtilityGridDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'datascale', 'utilitygridtype', 'other')
    list_filter    = ('datascale', 'utilitygridtype')
    search_fields  = ('id__id', 'other')


@admin.register(SRIOnsiteenergygeneration)
class SRIOnsiteenergygenerationAdmin(admin.ModelAdmin):
    list_display   = ('id', 'renewableenergy', 'nonrenewableenergy')
    list_filter    = ('renewableenergy', 'nonrenewableenergy')
    search_fields  = ('id__id',)


@admin.register(SRIInformationNeed)
class SRIInformationNeedAdmin(admin.ModelAdmin):
    list_display   = (
        'id',
        'descriptioninformationneed',
        'objectclass',
    )
    search_fields  = (
        'id__id',
        'descriptioninformationneed',
        'objectclass__classname',
    )
    raw_id_fields  = ('objectclass', )


@admin.register(SRIUsecase)
class SRIUsecaseAdmin(admin.ModelAdmin):
    list_display   = ('id', 'title', 'description')
    search_fields  = ('id__id', 'title', 'description')
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
