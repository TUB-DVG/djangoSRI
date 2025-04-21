## This file contains all the models reagarding the information need of the SRI project.
from django.db import models
from citydb.modules.core.cityobject import CityObject
from citydb.modules.core.objectclass import ObjectClass

# SRI_informationneed model (base class for information need models)
class SRIInformationNeed(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id', null=True)

    class Meta:
        db_table = 'sri_informationneed'
        indexes = [
            models.Index(fields=['objectclass']),
        ]

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
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    objectclass = models.ForeignKey(ObjectClass, on_delete=models.CASCADE, db_column='objectclass_id', null=True)

    class Meta:
        db_table = 'sri_datasource'
        indexes = [
            models.Index(fields=['objectclass']),
        ]

# SRI_model model (inherits from SRIDataSource)
# To-Do: Rework the model that work for this
class SRIModel(models.Model):
    id = models.OneToOneField(SRIDataSource, primary_key=True, on_delete=models.CASCADE, db_column='id')

    class Meta:
        db_table = 'sri_model'

# SRI_interface model
class SRIInterface(models.Model):
    id = models.OneToOneField(SRIDataSource, primary_key=True, on_delete=models.CASCADE, db_column='id')
    supportedaccesst_description = models.CharField(max_length=1000, blank=True, null=True)
    supportedaccesst_hasendpoint = models.IntegerField(blank=True, null=True)
    supportedaccesstype_hasapi = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sri_interface'

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
        indexes = [
            models.Index(fields=['objectclass']),
        ]

# SRI_dataconnector model
class SRIDataConnector(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    modelschema = models.CharField(max_length=1000, blank=True, null=True)
    urlmodelschema = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'sri_dataconnector'