from django.db import models

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
        db_table = 'SRI_assessor'




# SRI_building model
class SRIBuilding(models.Model):
    """
    Model representing a building in the Smart Readiness Indicator (SRI) assessment.
    
    This model extends the Building model with SRI-specific attributes such as
    building state, usage type, climate zone, and other characteristics needed
    for SRI assessment calculations.
    
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
    
    # One-to-one relationship with Building model
    id = models.OneToOneField(Building, primary_key=True, on_delete=models.CASCADE, db_column='id')
    
    # Building characteristics fields
    buildingstate = models.CharField(max_length=1000, blank=True, null=True, choices=buildingstate_tag_choices)
    buildingusage = models.CharField(max_length=1000, blank=True, null=True, choices=sribuildingusage_tag_choices)
    climatezone = models.CharField(max_length=1000, blank=True, null=True, choices=climatezone_tag_choices)
    location = models.CharField(max_length=1000, blank=True, null=True)
    sribuildingtype = models.CharField(max_length=1000, blank=True, null=True, choices=sribuildingtype_tag_choices)
    usefulfloorarea = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, 
                                         help_text="Useful floor area in square meters")

    class Meta:
        db_table = 'SRI_building'
        
    def __str__(self):
        """Return a string representation of the SRI building."""
        return f"SRI Building {self.id_id}"



# SRI_functionalitylevel model
class SRIFunctionalitylevel(models.Model):

    functionalitylevel_tag_choices = (
        ("Functionality level 0", "Functionality level 0 (as non-smart default)"),
        ("functionalityLevel1", "Functionality level 1"),
        ("functionalityLevel2", "Functionality level 2"),
        ("functionalityLevel3", "Functionality level 3"),
        ("functionalityLevel4", "Functionality level 4")
    )

    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    functionalitylevel = models.IntegerField(blank=True, null=True)
    id_1 = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_functionalitylevel'


# SRI_methodology model
class SRIMethodology(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    preferredservicecatalogue = models.CharField(max_length=1000, blank=True, null=True)
    preferredweightings = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_methodology'




# SRI_sriassessment model
class SRISriassessment(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    assessor_assessments = models.ForeignKey(
        SRIAssessor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='assessor_assessments_id',
        related_name='sri_assessments'
    )
    dateofassessment = models.DateTimeField(null=True, blank=True)
    fullbuilding = models.IntegerField(null=True, blank=True)
    methodology_assessments = models.ForeignKey(
        SRIMethodology,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='methodology_assessments_id',
        related_name='sri_assessments'
    )
    score = models.IntegerField(null=True, blank=True)
    sriservice_assessments = models.ForeignKey(
        'SRISriservice',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sriservice_assessments_id',
        related_name='sri_assessments'
    )

    class Meta:
        db_table = 'SRI_sriassessment'
        indexes = [
            models.Index(fields=['assessor_assessments']),
            models.Index(fields=['methodology_assessments']),
            models.Index(fields=['sriservice_assessments']),
        ]


# SRI_sriservice model
class SRISriservice(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    code = models.CharField(max_length=1000, blank=True, null=True)
    domain = models.CharField(max_length=1000, blank=True, null=True)
    impact = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    partofmethod = models.IntegerField(null=True, blank=True)
    partofmethodb = models.IntegerField(null=True, blank=True)
    preconditions = models.CharField(max_length=1000, blank=True, null=True)
    servicegroup = models.CharField(max_length=1000, blank=True, null=True)
    sriassessment_sriservices = models.ForeignKey(
        SRISriassessment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sriassessment_sriservices_id',
        related_name='sri_services'
    )
    userdefined = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'SRI_sriservice'
        indexes = [
            models.Index(fields=['sriassessment_sriservices']),
        ]


# SRI_usecase model
class SRIUsecase(models.Model):
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    description = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_usecase'


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
        ("domesticHotWater", "Domestic Hot Water")
    )
    
    id = models.OneToOneField(CityObject, primary_key=True, on_delete=models.CASCADE, db_column='id')
    category = models.CharField(max_length=1000, blank=True, null=True, choices=sri_domain_choices)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'SRI_domain'
