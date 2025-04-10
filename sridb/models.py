from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Constants for Technical Domains and Desired Impacts
TECHNICAL_DOMAINS = [
    ("heating", "Heating"),
    ("cooling", "Cooling"),
    ("domestic_hot_water", "Domestic Hot Water"),
    ("ventilation", "Ventilation"),
    ("lighting", "Lighting"),
    ("dynamic_building_envelope", "Dynamic Building Envelope"),
    ("electricity", "Electricity"),
    ("electric_vehicle_charging", "Electric Vehicle Charging"),
    ("monitoring_control", "Monitoring & Control"),
]

DOMAIN_PRESENCE_CHOICES = [
    (1, "Present"),
    (2, "Absent but Mandatory"),
    (0, "Absent and Not Mandatory"),
]

DESIRED_IMPACTS = [
    ("energy_efficiency", "Energy Efficiency"),
    ("maintenance_fault_prediction", "Maintenance & Fault Prediction"),
    ("comfort", "Comfort"),
    ("convenience", "Convenience"),
    ("health", "Health"),
    ("wellbeing_accessibility", "Well-being & Accessibility"),
    ("information_to_occupants", "Information to Occupants"),
    ("energy_flexibility_storage", "Energy Flexibility & Storage"),
]

class Assessor(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    certification_id = models.CharField(max_length=50, blank=True, null=True)

class AssessmentMethod(models.Model):
    method_type = models.CharField(max_length=50)  # "Audit", "Simulation"
    description = models.TextField(blank=True, null=True)

class EnergySystem(models.Model):
    system_type = models.CharField(max_length=50)  # "Heating", "Lighting"
    efficiency_score = models.FloatField()

class DomainPreference(models.Model):
    """Represents the presence and weighting of a technical domain in an assessment"""
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='domain_preferences')
    domain = models.CharField(max_length=50, choices=TECHNICAL_DOMAINS)
    presence_status = models.IntegerField(
        choices=DOMAIN_PRESENCE_CHOICES,
        default=0,
        help_text="1: Present, 2: Absent but Mandatory, 0: Absent and Not Mandatory"
    )
    weighting = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text="Domain weighting between 0 and 1"
    )

    class Meta:
        unique_together = ['assessment', 'domain']

    def __str__(self):
        return f"{self.domain} - Status: {self.get_presence_status_display()} (Weight: {self.weighting})"

class Assessment(models.Model):
    category = models.CharField(max_length=50)
    score = models.FloatField()
    description = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    valid_until = models.DateTimeField()
    method = models.ForeignKey(AssessmentMethod, on_delete=models.CASCADE)
    assessor = models.ForeignKey(Assessor, on_delete=models.CASCADE)
    preferred_service_catalogue = models.CharField(max_length=100, blank=True, null=True)

    def get_domain_preference(self, domain):
        """Get the preference status and weighting for a specific domain"""
        try:
            pref = self.domain_preferences.get(domain=domain)
            return {
                'status': pref.presence_status,
                'weighting': pref.weighting
            }
        except DomainPreference.DoesNotExist:
            return None

    def set_domain_preference(self, domain, status, weighting):
        """Set or update the preference for a specific domain"""
        DomainPreference.objects.update_or_create(
            assessment=self,
            domain=domain,
            defaults={
                'presence_status': status,
                'weighting': weighting
            }
        )

class SRILevel(models.Model):
    """SRI Level must be between 0 and 5. Also defines if valid for BuildingParts."""
    level_name = models.CharField(max_length=50, unique=True)
    level_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])  # Value between 0-5
    valid_for_building_part = models.BooleanField(default=False)  # Can be used for BuildingPart?

    def __str__(self):
        return f"{self.level_name} (Level {self.level_value})"

class Service(models.Model):
    """Represents a smart-ready service in one of 9 technical domains and 7 desired impacts"""
    name = models.CharField(max_length=100)
    sri_level = models.ForeignKey(SRILevel, on_delete=models.CASCADE)
    service_id = models.CharField(max_length=20, unique=True)
    functionality_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    description = models.ForeignKey('FunctionalityDescription', on_delete=models.SET_NULL, null=True, blank=True)
    technical_domain = models.CharField(max_length=50, choices=TECHNICAL_DOMAINS)
    desired_impact = models.CharField(max_length=50, choices=DESIRED_IMPACTS)
    
    # New fields for service requirements
    is_applicable = models.BooleanField(default=True)
    preconditions = models.TextField(blank=True, null=True)
    triage_score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)],
        help_text="0-3 score indicating if service affects maximum obtainable score",
        default=0
    )
    part_a = models.BooleanField(default=False, help_text="A-1: YES, 0-NO")
    part_b = models.BooleanField(default=False, help_text="B-1: YES, 0-NO")
    part_c = models.BooleanField(default=False, help_text="Part of the custom services list")

    def __str__(self):
        return f"{self.service_id} - {self.name} ({self.technical_domain})"

    class Meta:
        ordering = ['technical_domain', 'service_id']

class ServiceGroup(models.Model):
    """Groups related services within a domain"""
    name = models.CharField(max_length=100)
    technical_domain = models.CharField(max_length=50, choices=TECHNICAL_DOMAINS)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        unique_together = ['technical_domain', 'code']

class FunctionalityLevel(models.Model):
    """Defines the functionality levels (0-4) for a service"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='functionality_levels')
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    description = models.TextField()
    is_non_smart_default = models.BooleanField(default=False)

    class Meta:
        unique_together = ['service', 'level']
        ordering = ['level']

    def __str__(self):
        return f"{self.service.service_id} - Level {self.level}"


class FunctionalityDescription(models.Model):
    meta_service = models.ForeignKey("Service", on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)])
    description = models.TextField()

class BuildingInformation(models.Model):
    """Contains general information about a building or building part"""
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    climate_zone = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year_of_construction = models.IntegerField(null=True, blank=True)
    total_floor_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    number_of_floors = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Building Info: {self.location} ({self.climate_zone})"

    def clone(self):
        """Create a copy of this BuildingInformation instance"""
        return BuildingInformation.objects.create(
            location=self.location,
            latitude=self.latitude,
            longitude=self.longitude,
            climate_zone=self.climate_zone,
            description=self.description,
            year_of_construction=self.year_of_construction,
            total_floor_area=self.total_floor_area,
            number_of_floors=self.number_of_floors
        )

class Building(models.Model):
    building_id = models.CharField(max_length=50, unique=True) # GML ID
    building_info = models.OneToOneField(BuildingInformation, on_delete=models.CASCADE)
    sri_level = models.ForeignKey(SRILevel, on_delete=models.CASCADE)
    assessments = models.ManyToManyField(Assessment)
    energy_systems = models.ManyToManyField(EnergySystem)
    services = models.ManyToManyField(Service)  # Link smart services to buildings
    has_building_part = models.BooleanField(default=False)
    list_of_building_parts = models.ManyToManyField("BuildingPart", blank=True)

    def get_building_info(self):
        """Get the building information for this building"""
        return self.building_info

    def to_pydantic(self):
        """Converts Django Object to Pydantic Object"""
        from sri.pydantic_models import PydanticBuilding, SmartReadinessIndicator
        return PydanticBuilding(
            building_id=self.building_id,
            geometry=self.geometry,
            sri=SmartReadinessIndicator(
                building_id=self.building_id,
                assessments=[a.category for a in self.assessments.all()]
            ),
            energy_systems=[{"system_type": es.system_type, "efficiency_score": es.efficiency_score} for es in self.energy_systems.all()],
            service_level=self.sri_level.level_name
        )

    def __str__(self):
        return f"Building {self.building_id} - SRI Level {self.sri_level.level_value}"

class BuildingPart(Building):
    """A BuildingPart inherits from Building but has a parent building"""
    parent_building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="building_parts")
    override_building_info = models.OneToOneField(
        BuildingInformation, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='building_part_override'
    )

    def get_building_info(self):
        """
        Get the building information for this part.
        Returns override info if it exists, otherwise returns parent's info
        """
        return self.override_building_info or self.parent_building.get_building_info()

    def inherit_parent_info(self):
        """Create a new BuildingInformation instance based on parent's info"""
        if not self.override_building_info:
            parent_info = self.parent_building.get_building_info()
            self.override_building_info = parent_info.clone()
            self.save()

    def reset_to_parent_info(self):
        """Remove override and revert to parent's building information"""
        if self.override_building_info:
            self.override_building_info.delete()
            self.override_building_info = None
            self.save()

    def __str__(self):
        return f"BuildingPart {self.building_id} of {self.parent_building.building_id}"

class ServiceCatalog(models.Model):
    """Represents a collection of services for a specific version/standard"""
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    publication_date = models.DateField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['name', 'version']

    def __str__(self):
        return f"{self.name} v{self.version}"

class ServiceDefinition(models.Model):
    """Stores the base definition of a service that can be implemented"""
    catalog = models.ForeignKey(ServiceCatalog, on_delete=models.CASCADE, related_name='services')
    service_id = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    technical_domain = models.CharField(max_length=50, choices=TECHNICAL_DOMAINS)
    service_group = models.ForeignKey(ServiceGroup, on_delete=models.CASCADE, related_name='services')
    desired_impact = models.CharField(max_length=50, choices=DESIRED_IMPACTS)
    description = models.TextField(blank=True, null=True)
    
    # Service requirements
    is_applicable = models.BooleanField(default=True)
    preconditions = models.TextField(blank=True, null=True)
    triage_score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)],
        help_text="0-3 score indicating if service affects maximum obtainable score",
        default=0
    )
    part_a = models.BooleanField(default=False, help_text="A-1: YES, 0-NO")
    part_b = models.BooleanField(default=False, help_text="B-1: YES, 0-NO")
    part_c = models.BooleanField(default=False, help_text="Part of the custom services list")

    class Meta:
        unique_together = ['catalog', 'service_id']
        ordering = ['technical_domain', 'service_id']

    def __str__(self):
        return f"{self.service_id} - {self.name}"

class FunctionalityLevelDefinition(models.Model):
    """Defines the possible functionality levels for a service definition"""
    service_definition = models.ForeignKey(ServiceDefinition, on_delete=models.CASCADE, related_name='functionality_levels')
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(4)],
        help_text="Functionality level (0-4)"
    )
    description = models.TextField()
    is_non_smart_default = models.BooleanField(
        default=False,
        help_text="Indicates if this is the non-smart default level (usually level 0)"
    )

    class Meta:
        unique_together = ['service_definition', 'level']
        ordering = ['level']

    def __str__(self):
        return f"{self.service_definition.service_id} Level {self.level}"

class ServiceImplementation(models.Model):
    """Represents the actual implementation of a service in a building"""
    building = models.ForeignKey('Building', on_delete=models.CASCADE, related_name='implemented_services')
    service_definition = models.ForeignKey(ServiceDefinition, on_delete=models.PROTECT)
    current_functionality_level = models.ForeignKey(
        FunctionalityLevelDefinition, 
        on_delete=models.PROTECT,
        related_name='implementations'
    )
    implementation_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['building', 'service_definition']

    def __str__(self):
        return f"{self.service_definition.service_id} in {self.building.building_id} - Level {self.current_functionality_level.level}"
