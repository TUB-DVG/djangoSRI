## This file contains all the models reagarding the information need of the SRI project.
from django.db import models
from citydb.modules.core.cityobject import CityObject
from citydb.modules.core.objectclass import ObjectClass

# Defined outside the model as both indoor and 
# outdoor environmental models refer to this tag

environmentaldatatype_tag_choices = (
        ("thermal", "Thermal"),
        ("visual", "Visual"),
        ("airQuality", "Air Quality"),
        ("acoustic", "Acoustic"),
        ("noise", "Noise"),
        ("solar", "Solar"),
        ("other", "Other"),
        ("wind", "Wind"),
    )

# SRI_assetdata model
class SRIAssetData(models.Model):
    """
    Refering to the category Building and System Asset Data:

    Model represents the information tags available in the SRI_assetdata table.
    
    This model stores information about different types of assets related to SRI,
    including building characteristics, system characteristics, and other asset types.
    """
    
    asset_tag_choices = (
        ("buildingCharacteristics", "Building Characteristics"),
        ("systemCharacteristics", "System Characteristics"),
        ("other", "Other")
    )



    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    assettype = models.CharField(max_length=1000, blank=True, null=True, choices=asset_tag_choices)
    other = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_assetdata'


# SRI_indoorenvironmentalda model
class SRIIndoorEnvironmentalData(models.Model):

    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    environmentaldatatype = models.CharField(max_length=1000, blank=True, null=True,
                                              choices=environmentaldatatype_tag_choices)
    other = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_indoorenvironmentalda'


# SRI_controllogic model
class SRIControlLogic(models.Model):
    # id is FK to SRIDatacategorymeta
    controlsystem_tag_choices = (
        ("hvac", "HVAC"),
        ("lighting", "Lighting"),
        ("fenestration", "Fenestration"),
        ("plant", "Plant"),
        ("other", "Other")
    )
    controltype_tag_choices = (
        ("logic", "Logic"),
        ("setpoint", "Setpoint"),
        ("schedule", "Schedule"),
        ("other", "Other")
    )
    id = models.OneToOneField('SRIDatacategorymeta', primary_key=True, on_delete=models.CASCADE, db_column='id')
    controlsystem = models.CharField(max_length=1000, blank=True, null=True, choices=controlsystem_tag_choices)
    controltype = models.CharField(max_length=1000, blank=True, null=True, choices=controltype_tag_choices)

    class Meta:
        db_table = 'SRI_controllogic'


# SRI_cyberdevicedata model
class SRICyberDeviceData(models.Model):
    cyberdevicetype_tag_choices = ( 
        ("proxy", "Proxy"),
        ("cyberAttack", "Cyber Attack"),
        ("other", "Other")   
    )
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    cyberdevicetype = models.CharField(max_length=1000, blank=True, null=True, choices=cyberdevicetype_tag_choices)
    other = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_cyberdevicedata'


# SRI_datacategorymeta model
class SRIDatacategoryMeta(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    datascale = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    designtype = models.CharField(max_length=1000, blank=True, null=True)
    # ForeignKey to ObjectClass using the column objectclass_id
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id')
    occupanttype = models.CharField(max_length=1000, blank=True, null=True)
    other = models.CharField(max_length=1000, blank=True, null=True)
    utilitygridtype = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_datacategorymeta'
        indexes = [
            models.Index(fields=['objectclass']),
        ]


# SRI_energydata model
class SRIEnergyData(models.Model):
    # id is FK to SRIDatacategorymeta
    enduse_tag_choices = (
        ("hvac  ", "HVAC"),
        ("lighting", "Lighting"),
        ("appliances", "Appliances"),
        ("DHW", "DHW"),
        ("Pump", "Pumps"),
        ("ventilation", "Ventilation"),
        ("other", "Other")
    )
    energysource_tag_choices = (
        ("fuel", "Fuel"),
        ("electricity", "Electricity"),
        ("other", "Other")
    )
    id = models.OneToOneField(SRIDatacategoryMeta, primary_key=True, on_delete=models.CASCADE, db_column='id')
    enduse = models.CharField(max_length=1000, blank=True, null=True, choices=enduse_tag_choices)
    energysource = models.CharField(max_length=1000, blank=True, null=True)
    scale = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_energydata'


# SRI_operationaldata model
class SRIOperationalData(models.Model):
    # id is FK to SRIDatacategorymeta
    systemdata_tag_choices = (
        ("hvac", "HVAC"),
        ("lighting", "Lighting"),
        ("fenestration", "Fenestration"),
        ("plant", "Plant"),
        ("hotWater", "Hot Water"),
        ("nonHeatedWater", "Non Heated Water"),
        ("equipment", "Equipment"),
        ("energyStorage", "Energy Storage"),
        ("other", "Other")
    )
    systemtype_tag_choices = (
        ("log", "Log"),
        ("fault", "Fault"),
        ("other", "Other")
    )

    id = models.OneToOneField(SRIDatacategoryMeta, primary_key=True, on_delete=models.CASCADE, db_column='id')
    systemdata = models.CharField(max_length=1000, blank=True, null=True)
    systemtype = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_operationaldata'


# SRI_outdoorenvironmentald model
class SRIOutdoorenvironmentalData(models.Model):
    

    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    environmentaldatatype = models.CharField(max_length=1000, blank=True, null=True)
    other = models.CharField(max_length=1000, blank=True, null=True)
    source = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_outdoorenvironmentald'

# SRI_onsiteenergygeneratio model
class SRIOnsiteenergygeneratio(models.Model):
    renewableenergy_tag_choices = (
        ("solarEnergy", "Solar Energy"),
        ("windEnergy", "Wind Energy"),
        ("thermalEnergy", "Thermal Energy"),
        ("otherRenewableEnergy", "Other Renewable Energy")
    )
    nonrenewableenergy_tag_choices = (
        ("onSiteConventionalEnergy", "On-site Conventional Energy"),
        ("otherNonRenewableEnergy", "Other Non-Renewable Energy")
    )
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    nonrenewableenergy = models.CharField(max_length=1000, blank=True, null=True, choices=nonrenewableenergy_tag_choices)
    renewableenergy = models.CharField(max_length=1000, blank=True, null=True, choices=renewableenergy_tag_choices)

    class Meta:
        db_table = 'SRI_onsiteenergygeneratio'

