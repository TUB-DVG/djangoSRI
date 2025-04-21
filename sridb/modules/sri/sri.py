from django.db import models
from django.core import validators
from citydb.modules.core.cityobject import CityObject

from citydb.modules.bldg.building import Building
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
        
    def __str__(self):
        """Return a string representation of the SRI building."""
        return f"SRI Building {self.pk}"
        
    @property
    def assessments(self):
        """Property to access assessments through the reverse relation.
        This helps resolve potential naming conflicts.
        """
        # pylint: disable=no-member
        return self.sri_assessments.all()


# SRI_domain model
class SRIDomain(models.Model):

    # Does it make sense to have other as a choice?
    sri_domain_choices = (
        ("dynamicBuildingEnvelope", "Dynamic Building Envelope"),
        ("heating", "Heating"),
        ("electricVehicleCharging", "Electric Vehicle Charging"),
        ("cooling", "Cooling"),
        ("lighting", "Lighting"),
        ("monitoringAndControl", "Monitoring and Control"),
        ("ventilation", "Ventilation"),
        ("domesticHotWater", "Domestic Hot Water"),
        ("electricity", "Electricity")
    )
    
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    category = models.CharField(max_length=1000, blank=True, null=True, choices=sri_domain_choices)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_domain'





# SRI_methodology model
class SRIMethodology(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    preferredservicecatalogue = models.CharField(max_length=1000, blank=True, null=True)
    preferredweightings = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_methodology'


# SRI_sriservice model - moved before SRISriAssessment to fix forward references
class SRIServiceCatalogue(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True,
                              on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    version = models.FloatField(blank=True, null=True, validators=[
        validators.MinValueValidator(0.1, message="Version must be greater than 0")
    ])

    class Meta:
        db_table = 'sri_sriservicecatalogue'


class SRISriservice(models.Model):
    # Primary key is AutoField
    id = models.AutoField(primary_key=True)
    catalogue = models.ForeignKey(
        SRIServiceCatalogue,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='sri_services',
        db_column='sriservicecatalo_services_id'
    )
    additonalassesssedfunctional = models.IntegerField(null=True, blank=True)
    assesssedfunctionalitylevel = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=1000, blank=True, null=True)
    domaintype_category = models.CharField(max_length=1000, blank=True, null=True)
    domaintype_description = models.CharField(max_length=1000, blank=True, null=True)
    impact = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    objectclass_id = models.IntegerField(null=True, blank=True)
    partofmethod = models.IntegerField(null=True, blank=True)
    partofmethodb = models.IntegerField(null=True, blank=True)
    preconditions = models.CharField(max_length=1000, blank=True, null=True)
    servicegroup = models.CharField(max_length=1000, blank=True, null=True)
    shareadditionalfunctionality = models.IntegerField(null=True, blank=True)
    sharemainfunctionalitylevel = models.IntegerField(null=True, blank=True)
    userdefined = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'sri_sriservice'
        indexes = [
            models.Index(fields=['catalogue']),
        ]


# SRI_sriassessment model
class SRISriAssessment(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True,
                              on_delete=models.CASCADE, db_column='id')
    # Link assessment to buildings (Direct M2M relationship)
    buildings = models.ManyToManyField(
        Building,
        related_name='assessments',
        blank=True
    )
    # The sri_building field doesn't exist in the actual database schema, so remove it
    # sri_building = models.ForeignKey(
    #     SRIBuilding,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     db_column='sri_building',
    #     related_name='sri_assessments'
    # )
    assessor_assessments = models.ForeignKey(
        SRIAssessor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='assessor_assessments_id',
        related_name='sri_assessments'
    )
    dateofassessment = models.DateTimeField(null=True, blank=True)
    methodology_assessments = models.ForeignKey(
        SRIMethodology,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='methodology_assessments_id',
        related_name='sri_assessments'
    )
    score = models.IntegerField(null=True, blank=True)
    # Link assessment to multiple services (ManyToMany) with explicit through model
    sri_services = models.ManyToManyField(
        SRISriservice,
        blank=True,
        related_name='sri_assessments',
    )

    class Meta:
        db_table = 'sri_sriassessment'
        indexes = [
            models.Index(fields=['assessor_assessments']),
            models.Index(fields=['methodology_assessments']),
        ]


# SRI_usecase model
class SRIUsecase(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_usecase'



# SRI_functionalitylevel model
class SRIFunctionalitylevel(models.Model):

    functionalitylevel_tag_choices = (
        ("Functionality level 0", "Functionality level 0 (as non-smart default)"),
        ("functionalityLevel1", "Functionality level 1"),
        ("functionalityLevel2", "Functionality level 2"),
        ("functionalityLevel3", "Functionality level 3"),
        ("functionalityLevel4", "Functionality level 4")
    )

    # Primary key is AutoField
    id = models.AutoField(primary_key=True)
    # ForeignKey to SRISriservice
    sri_service = models.ForeignKey(
        SRISriservice,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='functionality_levels',
        db_column='sriservice_functionalityl_id'
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    functionalitylevel = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sri_functionalitylevel'
        indexes = [
            models.Index(fields=['sri_service']),
        ]
