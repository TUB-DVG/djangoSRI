from django.db import models
from django.core import validators
from citydb.modules.core.cityobject import CityObject
from citydb.modules.bldg.building import Building
from citydb.modules.core.objectclass import ObjectClass
# ToDo Double check if all choices are implemented correctly


# SRI_assessor model
class SRIAssessor(models.Model):
    # id is both PK and FK to cityobject
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    email = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    organisation = models.CharField(max_length=1000, blank=True, null=True)
    phonenumber = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_assessor'
        managed = False  # Since the table already exists in the database


# SRI_building model
class SRIBuilding(models.Model):
    """
    Model representing a building in the Smart Readiness Indicator (SRI) assessment.
    
    This model is linked to the Building model with a OneToOneField relation.
    The SRIBuilding contains SRI-specific attributes such as building state, 
    usage type, climate zone, and other characteristics needed for SRI assessment.
    
    The model uses predefined choice fields to ensure data consistency and
    facilitate standardized SRI assessments across different building types.
    """
    
    # Climate zone choices for SRI assessment
    climatezone_tag_choices = (
        ("NorthEastEurope", "North East Europe"),
        ("NorthEurope", "North Europe"),
        ("WestEurope", "West Europe"),
        ("SouthEastEurope", "South East Europe"),
        ("SouthEurope", "South Europe"),
        ("Other", "Other")
    )

    # Building state/renovation status choices
    buildingstate_tag_choices = (
        ("Original", "Original"),
        ("NormalRefurbishment", "Normal Refurbishment"),
        ("AdvancedRefurbishment", "Advanced Refurbishment"),
        ("Other", "Other")
    )

    # Building type classification choices
    sribuildingtype_tag_choices = (
        ("Residential", "Residential"),
        ("NonResidential", "Non-Residential"),
        ("Other", "Other")
    )
    
    # Detailed building usage classification choices
    sribuildingusage_tag_choices = ( 
        ("NonResidentialEducational", "Non-Residential Educational"),
        ("NonResidentialHealthcare", "Non-Residential Healthcare"),
        ("NonResidentialOffice", "Non-Residential Office"),
        ("ResidentialLargeMultiFamilyHouse", "Residential Large Multi-Family House"),
        ("ResidentialSmallMultiFamilyHouse", "Residential Small Multi-Family House"),
        ("ResidentialSingleFamilyHouse", "Residential Single-Family House"),
        ("ResidentialOther", "Residential Other"),
        ("Other", "Other")
    )
    
    # Use OneToOneField to Building with the same primary key
    # This matches the database structure where sri_building.id relates to building.id
    id = models.OneToOneField(Building, primary_key=True, on_delete=models.CASCADE, db_column='id')
    
    # Building characteristics fields
    buildingstate = models.CharField(max_length=1000, blank=True, null=True, choices=buildingstate_tag_choices)
    buildingusage = models.CharField(max_length=1000, blank=True, null=True, choices=sribuildingusage_tag_choices)
    climatezone = models.CharField(max_length=1000, blank=True, null=True, choices=climatezone_tag_choices)
    location = models.CharField(max_length=1000, blank=True, null=True)
    sribuildingtype = models.CharField(max_length=1000, blank=True, null=True, choices=sribuildingtype_tag_choices)
    usefulfloorarea = models.CharField(max_length=1000, blank=True, null=True)
    sridescription = models.CharField(max_length=1000, blank=True, null=True, default="")

    class Meta:
        db_table = 'sri_building'
        managed = False  # Since the table already exists in the database
        
    def __str__(self):
        """Return a string representation of the SRI building."""
        return f"SRI Building {self.pk}"



# SRI_methodology model -> currently not included - put in service layer 
#class SRIMethodology(models.Model):
#    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
#    preferredservicecatalogue = models.CharField(max_length=1000, blank=True, null=True)#
#    preferredweightings = models.CharField(max_length=1000, blank=True, null=True)
#
#    class Meta:
#        db_table = 'sri_methodology'
        managed = False  # Since the table already exists in the database

# SRI_servicecatalogue model - moved before SRISriAssessment to fix forward references
class SRIServiceCatalogue(models.Model):
    id = models.OneToOneField(
        Building, 
        primary_key=True, 
        on_delete=models.CASCADE, 
        db_column='id'
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True, validators=[
        validators.MinValueValidator(0.1, message="Version must be greater than 0")
    ])

    class Meta:
        db_table = 'sri_servicecatalogue'
        managed = False  # Since the table already exists in the database


# SRI_sriassessment model
class SRISriAssessment(models.Model):
    """Model for SRI assessments"""
    id = models.OneToOneField(
        CityObject,
        primary_key=True,
        on_delete=models.CASCADE,
        db_column='id'
    )
    dateofassessment = models.DateTimeField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    assessor_id = models.ForeignKey(
        'SRIAssessor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='assessor_id'
    )
    buildings = models.ManyToManyField(
        'SRIBuilding',
        related_name='assessments',
        db_table='sri_sriassessment_building'
    )

    class Meta:
        db_table = 'sri_sriassessment'
        managed = False

    def __str__(self):
        return f"Assessment on {self.dateofassessment} (Score: {self.score})"

class SRISriservice(models.Model):
    """
    SRI Service assignment for a building
    """
    
    # — Choice fields —
    sri_domain_choices = (
        ("dynamicBuildingEnvelope", "Dynamic Building Envelope"),
        ("heating",                  "Heating"),
        ("electricVehicleCharging",  "Electric Vehicle Charging"),
        ("cooling",                  "Cooling"),
        ("lighting",                 "Lighting"),
        ("monitoringAndControl",     "Monitoring and Control"),
        ("ventilation",              "Ventilation"),
        ("domesticHotWater",         "Domestic Hot Water"),
        ("electricity",              "Electricity"),
        ("other",                    "Other"),
    )

    functionalitylevel_tag_choices = (
        (0, "Functionality level 0 (as non-smart default)"),
        (1, "Functionality level 1"),
        (2, "Functionality level 2"),
        (3, "Functionality level 3"),
        (4, "Functionality level 4")
    )


    # -- Primary Key --
    # To-Do: This leads to a mass import of CityObject instances.
    # This is not the intended behavior.
    # Rather they should all be linked to a Building instance.
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')

    # — Attributes —
    code                         = models.CharField(max_length=1000, blank=True, null=True)
    servicename                  = models.CharField(max_length=1000, blank=True, null=True)
    descriptionfunctionalityleve = models.CharField(max_length=1000, blank=True, null=True)
    functionalitylevel           = models.IntegerField(null=True, blank=True, choices=functionalitylevel_tag_choices)
    impact                       = models.CharField(max_length=1000, blank=True, null=True)
    _partofmethoda               = models.IntegerField(db_column='partofmethoda', null=True, blank=True)
    _partofmethodb               = models.IntegerField(db_column='partofmethodb', null=True, blank=True)
    preconditions                = models.CharField(max_length=1000, blank=True, null=True)
    servicegroup                 = models.CharField(max_length=1000, blank=True, null=True)
    sharefunctionalitylevel      = models.IntegerField(null=True, blank=True)
    sridomain                    = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        choices=sri_domain_choices
    )
    _userdefined                  = models.IntegerField(db_column='userdefined', null=True, blank=True)

    # — Relationships —
    catalogue = models.ForeignKey(
        'SRIServiceCatalogue', 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sri_services',
        db_column='servicecatal_ispartofcata_id'
    )
    assessment = models.ForeignKey(
        'SRISriAssessment',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='services',
        db_column='sriassessmen_ispartofasse_id'
    )

    #building = models.ForeignKey(
    #    'SRIBuilding',
    #    on_delete=models.SET_NULL,
    #    null=True,
    #    blank=True,
    #    related_name='services',
    #    db_column='building_sriservice_id'
    #)

    class Meta:
        db_table = 'sri_sriservice'
        managed = False  # Since the table already exists in the database

    @property
    def partofmethoda(self):
        """Return _is_cooled.

        Value is 1 if thermal zone has energy system for space
        cooling, else 0.
        """
        if self._partofmethoda is None:
            return None
        translate = {0: False, 1: True}
        value = translate[self._partofmethoda]
        return value
    
    @property
    def partofmethodb(self):
        """Return _is_partofmethodb.

        Value is 1 if thermal zone has energy system for space
        cooling, else 0.
        """
        if self._partofmethodb is None:
            return None
        translate = {0: False, 1: True,
                     True: True,
                     False: False,
                     "0": False,
                     "1": True}
        print(self._partofmethodb)
        value = translate[self._partofmethodb]
        return value
    
    @property
    def userdefined(self):
        """Return _is_userdefined.

        Value is 1 if thermal zone has energy system for space
        cooling, else 0.
        """
        if self._userdefined is None:
            return None
        translate = {0: False, 1: True,
                     True: True,
                     False: False}
        value = translate[self._userdefined]
        return value



