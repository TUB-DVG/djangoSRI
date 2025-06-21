## This file contains all the models reagarding the information need of the SRI project.
from django.db import models
from citydb.modules.core.cityobject import CityObject
from citydb.modules.core.objectclass import ObjectClass
from sridb.modules.sri.information_need import SRIInformationNeed


access_tag_choices = [
    ('API', 'API'),
    ('Endpoint', 'Endpoint'),
    ('Tool', 'Tool'),
    ('Other', 'Other'),
]


# SRI_informationneed model (base class for information need models)
#class SRIInformationNeed(models.Model):
#    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
#    description = models.CharField(max_length=1000, blank=True, null=True)
#    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id', null=True)#
#    class Meta:
#        db_table = 'sri_informationneed'
#        indexes = [
#            models.Index(fields=['objectclass']),
#        ]

# SRI_supportedaccess model
class SRISupportedAccess(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    hasapi = models.IntegerField(blank=True, null=True, db_column='hasapi')
    hasendpoint = models.IntegerField(blank=True, null=True, db_column='hasendpoint')

    class Meta:
        db_table = 'sri_supportedaccess'

# SRI_datasource model (base class for data sources)
class SRIDataSource(models.Model):
    cityobject_ptr_id= models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    #cityobject_ptr_id
    dataconnectort_documentation = models.CharField(max_length=1000, blank=True, null=True)
    dataconnectortyp_modelschema = models.CharField(max_length=1000, blank=True, null=True)
    dataconnectortype_modeluri = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id')

    class Meta:
        db_table = 'sri_datasource'
        indexes = [
            models.Index(fields=['objectclass']),
        ]

    #def save(self, *args, **kwargs):
    #    if not self.id_id:  # '_id' is added by Django for FK fields
    #        city_obj = CityObject.objects.create(...)
    #        self.id = city_obj
    #    super().save(*args, **kwargs)

# SRI_model model (inherits from SRIDataSource)
# To-Do: Rework the model that work for this
class SRIModel(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    aquisitionmethod = models.CharField(max_length=1000, blank=True, null=True)
    software = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_model'

# SRI_interface model
class SRIInterface(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    interfacetype = models.CharField(max_length=1000, blank=True, null=True)
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id')
    supportedaccesst_description = models.CharField(max_length=1000, blank=True, null=True)
    supportedaccesst_hasendpoint = models.IntegerField(blank=True, null=True)
    supportedaccessty_accesstype = models.CharField(max_length=1000, blank=True, null=True)
    supportedaccesstype_hasapi = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sri_interface'
        indexes = [
            models.Index(fields=['objectclass']),
        ]

# SRI_device model
class SRIDevice(models.Model):
    id = models.OneToOneField(SRIDataSource, primary_key=True, on_delete=models.CASCADE, db_column='id')
    manufacturer = models.CharField(max_length=1000, blank=True, null=True)
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id', null=True)
    supportedaccesst_description = models.CharField(max_length=1000, blank=True, null=True)
    supportedaccesst_hasendpoint = models.IntegerField(blank=True, null=True)
    supportedaccesstype_hasapi = models.IntegerField(blank=True, null=True)
    supportedprotcolls = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sri_device'

# SRI_dataconnector model
class SRIDataConnector(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    modelschema = models.CharField(max_length=1000, blank=True, null=True)
    urlmodelschema = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sri_dataconnector'


# To-Do: Fix Model to SRIIctEquipment
class SRIIctequipment(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    devicecategory = models.CharField(max_length=1000, blank=True, null=True)
    manufacturer = models.CharField(max_length=1000, blank=True, null=True)
    # To-Do: add option for multiple access types
    supportedaccesst_description = models.CharField(max_length=1000, blank=True, null=True, choices=access_tag_choices)
    supportedaccesst_hasendpoint = models.IntegerField(blank=True, null=True)
    supportedaccessty_accesstype = models.CharField(max_length=1000, blank=True, null=True)
    supportedaccesstype_hasapi = models.IntegerField(blank=True, null=True)
    supportedprotcols = models.CharField(max_length=1000, blank=True, null=True)
    
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id')
    

    class Meta:
        db_table = 'sri_ictequipment'

class SRICommunicationProtocol(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    protocoltype = models.CharField(max_length=1000, blank=True, null=True)
    protocolversion = models.CharField(max_length=1000, blank=True, null=True)
    ictequipment = models.ForeignKey(SRIIctequipment, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'sri_communicationprotocol'