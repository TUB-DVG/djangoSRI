import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
import pandas as pd
from sridb.modules.sri.sri import (
    SRISriservice,
    SRIBuilding
)
from sridb.management.commands.cityobject import get_or_create_building, get_or_create_cityobject

from sridb.modules.sri.information_need import (
    SRIAssetData, SRIIndoorEnvironmentalData, SRIControlLogic,
    SRICyberDeviceData, SRIEnergyData, SRIOperationalData,
    SRIOutdoorenvironmentalData, SRIOnsiteenergygeneration,
    SRIInformationNeed, SRIUtilityGridData,
    SRIInformationNeedData
)
# must add SRIUsecase, if put in database layer
from citydb.modules.core.objectclass import ObjectClass

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH_ARCHETYPE_CATALOGUE = os.path.join(PARENT_DIR, 'auxillary', 'archetypes', 'DigitalArchetypes_InformationNeed_v01.xlsx')
ARCHETYPE_CATALOGUE = pd.read_excel(PATH_ARCHETYPE_CATALOGUE, engine='openpyxl')

INFORMATION_NEED_COLUMNS =  ('Use Cases', 'Energy data',
                             'Indoor environmental data', 'Outdoor envionmental data', 'System and equipment operational data',
                             'Control setting and logic data', 'Occupant data', 'Design basis data',
                             'Building and system asset data', 'Utility and grid signal data',
                             'Onsite energy generation data', 'Cyber (IoT) device data')


INFORMATION_NEED_COLUMNS = (
    'Use Cases',
    'Energy data',
    'Indoor environmental data',
    'Outdoor envionmental data',
    'System and equipment operational data',
    'Control setting and logic data',
    'Occupant data',
    'Design basis data',
    'Building and system asset data',
    'Utility and grid signal data',
    'Onsite energy generation data',
    'Cyber (IoT) device data',
)

INFORMATION_NEED_OBJECTS = {
    "Energy data":                      SRIEnergyData,
    "Indoor environmental data":        SRIIndoorEnvironmentalData,
    "Outdoor envionmental data":        SRIOutdoorenvironmentalData,
    "System and equipment operational data": SRIOperationalData,
    "Control setting and logic data":   SRIControlLogic,
    "Occupant data":                    SRIDatacategoryMeta,
    "Design basis data":                SRIDatacategoryMeta,
    "Building and system asset data":   SRIAssetData,
    "Utility and grid signal data":     SRIUtilityGridData,
    "Onsite energy generation data":    SRIOnsiteenergygeneration,
    "Cyber (IoT) device data":          SRICyberDeviceData,
}


def build_choice_lookup_for_model(model_class):
    lookup = {}
    for field in model_class._meta.get_fields():
        if hasattr(field, 'choices') and field.choices:
            for key, label in field.choices:
                lookup[label.strip().lower()] = (field.name, key)
    return lookup


class Command(BaseCommand):
    help = 'Creates an archetype for a given data category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str, help='The data category to create an archetype for')

    def handle(self, *args, **options):
        category = options['category']
        
        # Map category names to their respective models
        category_map = {
            "Asset data":                     SRIAssetData,
            "Indoor environmental data":       SRIIndoorEnvironmentalData,
            "Outdoor environmental data":      SRIOutdoorenvironmentalData,
            "Control logic":                  SRIControlLogic,
            "Cyber device data":              SRICyberDeviceData,
            "Energy data":                    SRIEnergyData,
            "Operational data":               SRIOperationalData,
            "Utility grid data":              SRIUtilityGridData,
            "Onsite energy generation":       SRIOnsiteenergygeneration,
            "Information need":               SRIInformationNeed,
            "Information need data":          SRIInformationNeedData
        }
        # must add SRIUsecase, if put in database layer
        if category not in category_map:
            self.stdout.write(self.style.ERROR(f'Unknown category: {category}'))
            self.stdout.write(self.style.NOTICE('Available categories:'))
            for cat in category_map.keys():
                self.stdout.write(self.style.NOTICE(f'  - {cat}'))
            return

        model = category_map[category]
        
        # Create the archetype
        try:
            # Get the parent class if it exists
            parent = model.__bases__[0]
            
            # Create the object
            obj = model.objects.create()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created archetype for {category}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to create archetype: {str(e)}'))