from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, format_html_join
from django.urls import reverse

# Import SRI models from the updated structure
from sridb.modules.sri.sri import (
    SRIAssessor,
    SRIBuilding,
    #SRIMethodology,
    SRISriAssessment,

    SRIServiceCatalogue,
    SRISriservice
)

# Import Information Need models
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
    SRIInformationNeed,
    SRIUtilityGridData,
    SRIInformationNeedData,
    SRIDesignBasisData
)

# Import ICT models
from .modules.sri.ict import (
    SRIIctequipment,
    SRIDataSource,
    SRICommunicationProtocol,
    SRIInterface,
    SRIDevice,
    SRIDataConnector,
    SRIModel
)


@admin.register(SRIBuilding)
class SRIBuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buildingstate',
        'buildingusage',
        'climatezone',
        'sribuildingtype',
    )
    list_filter = (
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
    
    def get_assessments(self, obj):
        return ", ".join([str(assessment) for assessment in obj.assessments.all()])
    get_assessments.short_description = "Assessments"

@admin.register(SRISriAssessment)
class SRISriAssessmentAdmin(admin.ModelAdmin):
    list_display = ('dateofassessment', 'score', 'assessor_name', 'get_building')
    list_filter = ('dateofassessment', 'score')
    search_fields = ('assessor_id__name', 'buildings__id__id')
    raw_id_fields = ('assessor_id',)
    filter_horizontal = ('buildings',)
    
    class SRIServiceInline(admin.TabularInline):
        model = SRISriservice
        extra = 1
        fields = ('code', 'servicename', 'sridomain', 'servicegroup', 'functionalitylevel')
        verbose_name = "Service"
        verbose_name_plural = "Assessment Services"

    inlines = [SRIServiceInline]
    
    def assessor_name(self, obj):
        return obj.assessor_id.name if obj.assessor_id else "-"
    assessor_name.short_description = 'Assessor'

    def get_building(self, obj):
        buildings = obj.buildings.all()
        if buildings:
            return ', '.join(str(b.id) for b in buildings)
        return '-'
    get_building.short_description = 'Buildings'

# Assessor Admin
@admin.register(SRIAssessor)
class SRIAssessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organisation', 'email', 'phonenumber')
    search_fields = ('name', 'organisation', 'email')

# Methodology Admin - curenntly not included - in service layer 
#admin.register(SRIMethodology)
#class SRIMethodologyAdmin(admin.ModelAdmin):
#    list_display = ('id', 'preferredservicecatalogue', 'preferredweightings')
#    search_fields = ('preferredservicecatalogue', 'preferredweightings')


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
    list_filter = ('sridomain', 'servicegroup')
    search_fields = ('code', 'servicename', 'sridomain', 'descriptionfunctionalityleve')
    raw_id_fields = ('catalogue', 'assessment')
    fieldsets = (
        ('Basic Information', {
            'fields': ('code', 'servicename', 'sridomain', 'servicegroup')
        }),
        ('Relationships', {
            'fields': ('catalogue', 'assessment')
        }),
        ('Functionality', {
            'fields': ('functionalitylevel', 'descriptionfunctionalityleve', 'sharefunctionalitylevel')
        }),
        ('Method Settings', {
            'fields': ('_partofmethoda', '_partofmethodb', '_userdefined', 'preconditions')
        }),
    )
    
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
    list_display = ('id', 'assettype', 'other')
    list_filter = ('assettype',)
    search_fields = ('id__id__id', 'assettype', 'other')
    raw_id_fields = ('id',)

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


@admin.register(SRIEnergyData)
class SRIEnergyDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'enduse', 'energysource')
    list_filter    = ('enduse', 'energysource')
    search_fields  = ('id__id',)


@admin.register(SRIOperationalData)
class SRIOperationalDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'systemdata', 'systemtype', 'other', 'datascale')
    list_filter    = ('systemdata', 'systemtype', 'datascale')
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

@admin.register(SRIDesignBasisData)
class SRIDesignBasisDataAdmin(admin.ModelAdmin):
    list_display   = ('id', 'datascale', 'designtype', 'other')
    list_filter    = ('datascale', 'designtype')
    search_fields  = ('id__id', 'other')


@admin.register(SRIInformationNeed)
class SRIInformationNeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'descriptioninformationneed', 'sriservice_needs')
    search_fields = ('id__id', 'descriptioninformationneed')
    raw_id_fields = ('sriservice_needs',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('id', 'sriservice_needs')


#@admin.register(SRIUsecase) -> put to service layer
#class SRIUsecaseAdmin(admin.ModelAdmin):
#    list_display   = ('id', 'title', 'description')
#    search_fields  = ('id__id', 'title', 'description')

# Old data model
#@admin.register(SRISupportedAccess)
#class SRISupportedAccessAdmin(admin.ModelAdmin):
#    list_display = ('id', 'description', 'hasapi', 'hasendpoint')
#    search_fields = ('description',)

@admin.register(SRIDataSource)
class SRIDataSourceAdmin(admin.ModelAdmin):
    list_display = ('cityobject_ptr_id', 'name', 'description', 'objectclass')
    search_fields = ('cityobject_ptr_id__id', 'name', 'description')  
    raw_id_fields = ('objectclass', 'cityobject_ptr_id') 
    fieldsets = (
        ('Basic Information', {
            'fields': ('cityobject_ptr_id', 'name', 'description', 'objectclass')
        }),
        ('Data Connector', {
            'fields': ('dataconnectort_documentation', 'dataconnectortyp_modelschema', 'dataconnectortype_modeluri')
        }),
    )


@admin.register(SRIIctequipment)
class SRIIctequipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'devicecategory', 'manufacturer', 'objectclass')
    search_fields = ('id__id', 'devicecategory', 'manufacturer')
    raw_id_fields = ('objectclass', 'id')
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'devicecategory', 'manufacturer', 'objectclass')
        }),
        ('Access Types', {
            'fields': (
                'supportedaccesst_description',
                'supportedaccesst_hasendpoint',
                'supportedaccessty_accesstype',
                'supportedaccesstype_hasapi',
                'supportedprotcols'
            )
        }),
    )

@admin.register(SRICommunicationProtocol)
class SRICommunicationProtocolAdmin(admin.ModelAdmin):
    list_display = ('id', 'protocoltype', 'protocolversion')
    list_filter = ('protocoltype',)
    search_fields = ('protocoltype', 'protocolversion')


@admin.register(SRIInterface)
class SRIInterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'interfacetype', 'objectclass', 'supportedaccesst_hasendpoint', 'supportedaccesstype_hasapi')
    list_filter = ('interfacetype',)
    search_fields = ('id__id', 'interfacetype', 'supportedaccest_description')
    raw_id_fields = ('objectclass', 'id')
    fieldsets = (
        ('Basic Information', {
            'fields': ('id', 'interfacetype', 'objectclass')
        }),
        ('Access Settings', {
            'fields': ('supportedaccesst_description', 'supportedaccesst_hasendpoint',
                      'supportedaccessty_accesstype', 'supportedaccesstype_hasapi')
        }),
    )

@admin.register(SRIModel)
class SRIModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'aquisitionmethod', 'software', 'type', 'version')
    list_filter = ('type', 'software')
    search_fields = ('id__id', 'software', 'type', 'version')
    raw_id_fields = ('id',)
    fieldsets = (
        ('Model Information', {
            'fields': ('id', 'aquisitionmethod', 'software', 'type', 'version')
        }),
    )

@admin.register(SRIInformationNeedData)
class SRIInformationNeedDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'objectclass', 'information_datarequired')
    search_fields = ('id__id', 'objectclass__classname')
    raw_id_fields = ('objectclass', 'information_datarequired')


