from django.db import models
from citydb.modules.core.cityobject import CityObject
from citydb.modules.core.objectclass import ObjectClass


environmentaldatatype_tag_choices = (
    ("thermal",       "Thermal"),
    ("visual",        "Visual"),
    ("airQuality",    "Air Quality"),
    ("acoustic",      "Acoustic"),
    ("noise",         "Noise"),
    ("solar",         "Solar"),
    ("other",         "Other"),
    ("wind",          "Wind"),
)

scale_tag_choices = (
    ("room",              "Room"),
    ("building",          "Building"),
    ("district",          "District"),
    ("system",            "System"),
    ("floor",             "Floor"),
    ("otherSpatialScale", "Other Spatial Scale"),
    ("equipment",         "Equipment"),
    ("zone",              "Zone"),
    ("circuit",           "Circuit"),
)

renewableenergy_tag_choices = (
    ("solarEnergy",           "Solar Energy"),
    ("solar",                  "Solar"),
    ("windEnergy",            "Wind Energy"),
    ("wind",                  "Wind"),
    ("thermalEnergy",         "Thermal Energy"),
    ("thermal",               "Thermal"),
    ("otherRenewableEnergy",  "Other Renewable Energy"),
)

nonrenewableenergy_tag_choices = (
    ("onSiteConventionalEnergy", "On-site Conventional Energy"),
    ("otherNonRenewableEnergy",   "Other Non-Renewable Energy"),
)

controlsystem_tag_choices = (
    ("hvac",        "HVAC"),
    ("lighting",    "Lighting"),
    ("fenestration","Fenestration"),
    ("plant",       "Plant"),
    ("other",       "Other"),
)

controltype_tag_choices = (
    ("logic",    "Logic"),
    ("setpoint", "Setpoint"),
    ("schedule", "Schedule"),
    ("other",    "Other"),
)

asset_tag_choices = (
    ("buildingCharacteristics", "Building Characteristics"),
    ("systemCharacteristics",   "System Characteristics"),
    ("other",                   "Other"),
)

enduse_tag_choices = (
    ("hvac",      "HVAC"),
    ("lighting",  "Lighting"),
    ("appliances","Appliances"),
    ("DHW",       "DHW"),
    ("Pump",      "Pumps"),
    ("ventilation","Ventilation"),
    ("other",     "Other"),
)

energysource_tag_choices = (
    ("fuel",        "Fuel"),
    ("electricity", "Electricity"),
    ("other",       "Other"),
)

systemdata_tag_choices = (
    ("hvac",          "HVAC"),
    ("lighting",      "Lighting"),
    ("fenestration",  "Fenestration"),
    ("plant",         "Plant"),
    ("hotWater",      "Hot Water"),
    ("nonHeatedWater","Non Heated Water"),
    ("equipment",     "Equipment"),
    ("energyStorage", "Energy Storage"),
    ("other",         "Other"),
)

systemtype_tag_choices = (
    ("log",          "Log"),
    ("fault",        "Fault"),
    ("other",        "Other"),
)

utilitygridtype_tag_choices = (
    ("Tariff",         "Tariff"),
    ("DemandResponse", "Demand Response"),
    ("CarbonEmission", "Carbon Emission"),
    ("OtherUtilityGrid","Other Utility Grid"),
)

occupanttype_tag_choices = (
    ("Occupancy",  "Occupancy"),
    ("Actions",    "Actions"),
    ("Attributes", "Attributes"),
    ("Attitude",   "Attitude"),
    ("Other",      "Other"),
)

designtype_tag_choices = (
    ("IEQCriteria",      "IEQ Criteria"),
    ("DesignWeather",    "Design Weather"),
    ("Drawings",         "Drawings"),
    ("RatedPower",       "Rated Power"),
    ("Schedules",        "Schedules"),
    ("OtherDesign",      "Other Design"),
)


class SRIInformationNeed(models.Model):
    """
    Base table for all InformationNeed entries.
    """
    id = models.OneToOneField(
        CityObject,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    descriptioninformationneed = models.CharField(
        max_length=1000,
        db_column='descriptioninformationneed'
    )
    objectclass = models.ForeignKey(
        ObjectClass,
        on_delete=models.CASCADE,
        db_column='objectclass_id'
    )
    #usecase_informationneed = models.ForeignKey(
    #    SRIUsecase,
    #    on_delete=models.CASCADE,
    #    db_column='usecase_informationneed_id'
    #)

    class Meta:
        db_table = 'sri_informationneed'



class SRIAssetData(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    assettype = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=asset_tag_choices,
        db_column='assettype'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_assetdata'


class SRIIndoorEnvironmentalData(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    environmentaldatatype = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=environmentaldatatype_tag_choices,
        db_column='environmentaldatatype'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_indoorenvironmentalda'


class SRIOutdoorenvironmentalData(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    environmentaldatatype = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=environmentaldatatype_tag_choices,
        db_column='environmentaldatatype'
    )
    source = models.CharField(max_length=1000, blank=True, null=True, db_column='source')
    other  = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_outdoorenvironmentald'


class SRIControlLogic(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    controlsystem = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=controlsystem_tag_choices,
        db_column='controlsystem'
    )
    controltype = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=controltype_tag_choices,
        db_column='controltype'
    )
    datascale = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=scale_tag_choices,
        db_column='datascale'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_controllogic'


class SRIDatacategoryMeta(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    datascale = models.CharField(
        max_length=1000,
        blank=True, null=True,
        choices=scale_tag_choices,
        db_column='datascale'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_datacategorymeta'


class SRIEnergyData(models.Model):
    id = models.OneToOneField(
        SRIDatacategoryMeta,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    enduse       = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=enduse_tag_choices,
        db_column='enduse'
    )
    energysource = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=energysource_tag_choices,
        db_column='energysource'
    )

    class Meta:
        db_table = 'sri_energydata'


class SRIOperationalData(models.Model):
    id = models.OneToOneField(
        SRIDatacategoryMeta,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    systemdata = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=systemdata_tag_choices,
        db_column='systemdata'
    )
    systemtype = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=systemtype_tag_choices,
        db_column='systemtype'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_operationaldata'


class SRIUtilityGridData(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    datascale       = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=scale_tag_choices,
        db_column='datascale'
    )
    utilitygridtype = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=utilitygridtype_tag_choices,
        db_column='utilitygridtype'
    )
    other           = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_utilitygriddata'


class SRIOnsiteenergygeneration(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    nonrenewableenergy = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=nonrenewableenergy_tag_choices,
        db_column='nonrenewableenergy'
    )
    renewableenergy    = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=renewableenergy_tag_choices,
        db_column='renewableenergy'
    )

    class Meta:
        db_table = 'sri_onsiteenergygeneratio'


class SRICyberDeviceData(models.Model):
    id = models.OneToOneField(
        SRIInformationNeed,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    cyberdevicetype = models.CharField(
        max_length=1000, blank=True, null=True,
        choices=(
            ("proxy",       "Proxy"),
            ("cyberAttack", "Cyber Attack"),
            ("other",       "Other"),
        ),
        db_column='cyberdevicetype'
    )
    other = models.CharField(max_length=1000, blank=True, null=True, db_column='other')

    class Meta:
        db_table = 'sri_cyberdevicedata'


class SRIUsecase(models.Model):
    id = models.OneToOneField(
        CityObject,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    title       = models.CharField(max_length=1000, blank=True, null=True, db_column='title')
    description = models.CharField(max_length=1000, blank=True, null=True, db_column='description')

    class Meta:
        db_table = 'sri_usecase'
