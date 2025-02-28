from django.core.management.base import BaseCommand
from django.utils import timezone
from sri.models import (
    ServiceCatalog,
    ServiceGroup,
    ServiceDefinition,
    FunctionalityLevelDefinition,
)

class Command(BaseCommand):
    help = 'Populates the service catalog with predefined services'

    def handle(self, *args, **options):
        # Create or get the service catalog
        catalog, _ = ServiceCatalog.objects.get_or_create(
            name="Smart Readiness Indicator Standard Catalog",
            version="1.0",
            defaults={
                'publication_date': timezone.now().date(),
                'description': "Standard service catalog for SRI assessment"
            }
        )

        # Create heating service groups
        heat_control_group, _ = ServiceGroup.objects.get_or_create(
            name="Heat control - demand side",
            technical_domain="heating",
            code="H-1"
        )

        heat_prod_group, _ = ServiceGroup.objects.get_or_create(
            name="Control heat production facilities",
            technical_domain="heating",
            code="H-2"
        )

        info_group, _ = ServiceGroup.objects.get_or_create(
            name="Information to occupants and facility managers",
            technical_domain="heating",
            code="H-3"
        )

        # Create heating services
        self.create_h1a(catalog, heat_control_group)
        self.create_h1b(catalog, heat_control_group)
        self.create_h1c(catalog, heat_control_group)
        self.create_h1d(catalog, heat_control_group)
        self.create_h1f(catalog, heat_control_group)
        self.create_h2a(catalog, heat_prod_group)
        self.create_h2b(catalog, heat_prod_group)
        self.create_h2d(catalog, heat_prod_group)
        self.create_h3(catalog, info_group)
        self.create_h4(catalog, info_group)

        self.stdout.write(self.style.SUCCESS('Successfully populated service catalog'))

    def create_h1a(self, catalog, group):
        service, _ = ServiceDefinition.objects.get_or_create(
            catalog=catalog,
            service_id="H1a",
            defaults={
                'name': "Heat emission control",
                'technical_domain': "heating",
                'service_group': group,
                'desired_impact': "energy_efficiency",
                'part_a': True,
                'part_b': True,
                'triage_score': 0
            }
        )

        levels = [
            (0, "No automatic control", True),
            (1, "Central automatic control (e.g. central thermostat)", False),
            (2, "Individual room control (e.g. thermostatic valves, or electronic controller)", False),
            (3, "Individual room control with communication between controllers and to BACS", False),
            (4, "Individual room control with communication and occupancy detection", False)
        ]

        for level, description, is_default in levels:
            FunctionalityLevelDefinition.objects.get_or_create(
                service_definition=service,
                level=level,
                defaults={
                    'description': description,
                    'is_non_smart_default': is_default
                }
            )

    def create_h1b(self, catalog, group):
        service, _ = ServiceDefinition.objects.get_or_create(
            catalog=catalog,
            service_id="H1b",
            defaults={
                'name': "Emission control for TABS (heating mode)",
                'technical_domain': "heating",
                'service_group': group,
                'desired_impact': "energy_efficiency",
                'part_a': False,
                'part_b': True,
                'triage_score': 0,
                'preconditions': "Triage: not relevant in case of TABS. Mostly restricted to non-residential buildings"
            }
        )

        levels = [
            (0, "No automatic control", True),
            (1, "Central automatic control", False),
            (2, "Advanced central automatic control", False),
            (3, "Advanced central automatic control with intermittent operation and/or room temperature feedback control", False),
            (4, "Advanced central automatic control with intermittent operation and/or room temperature feedback control", False)
        ]

        for level, description, is_default in levels:
            FunctionalityLevelDefinition.objects.get_or_create(
                service_definition=service,
                level=level,
                defaults={
                    'description': description,
                    'is_non_smart_default': is_default
                }
            )

    # Add similar methods for other services (H1c, H1d, H1f, H2a, H2b, H2d, H3, H4)
    # Each following the same pattern but with their specific data 