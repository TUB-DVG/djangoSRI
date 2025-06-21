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
    SRIInformationNeedData, SRIDesignBasisData, SRIOccupantData
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
    "Occupant data":                    SRIOccupantData,
    "Design basis data":                SRIDesignBasisData,
    "Building and system asset data":   SRIAssetData,
    "Utility and grid signal data":     SRIUtilityGridData,
    "Onsite energy generation data":    SRIOnsiteenergygeneration,
    "Cyber (IoT) device data":          SRICyberDeviceData,
}

# Map of archetype categories to model classes
ARCHETYPE_MODELS = [
    SRIInformationNeed,
    SRIInformationNeedData,
    SRIAssetData,
    SRIIndoorEnvironmentalData,
    SRIOutdoorenvironmentalData,
    SRIControlLogic,
    SRICyberDeviceData,
    SRIEnergyData,
    SRIOperationalData,
    SRIUtilityGridData,
    SRIOnsiteenergygeneration,
    SRIDesignBasisData,
    SRIOccupantData,
]



def build_choice_lookup_for_model(model_class):
    lookup = {}
    for field in model_class._meta.get_fields():
        if hasattr(field, 'choices') and field.choices:
            for key, label in field.choices:
                lookup[label.strip().lower()] = (field.name, key)
    return lookup


class Command(BaseCommand):
    help = 'Generates all digital archetypes for a given building GML ID.'

    def add_arguments(self, parser):
        parser.add_argument('building_id', type=str, help='The GML ID of the building.')

    @transaction.atomic
    def handle(self, *args, **options):
        building_id = options['building_id']
        self.stdout.write(self.style.NOTICE(f"Generating digital archetypes for building: {building_id}"))

        try:
            # 1. Get the Building and its CityObject instance
            building = get_or_create_building(building_id)
            cityobject = building   # id is a OneToOneField to CityObject
            print(type(cityobject))  # Should be <class 'citydb.models.CityObject'>


            # 2. Optionally, get ObjectClass for SRI archetypes if you need to set it
            # objectclass = ObjectClass.objects.get(classname="YourClassName")

            # 3. Create instances for each archetype model, if they do not exist yet
            created = []
            for model in ARCHETYPE_MODELS:
                # If this model expects id to be a SRIInformationNeedData instance, adapt accordingly
                field = model._meta.get_field('id')
                rel_model = field.related_model
                instance = None

                # For archetypes that require SRIInformationNeedData as their ID, chain creation
                if rel_model.__name__ == 'SRIInformationNeedData':
                    # Create a SRIInformationNeed if it does not exist
                    infoneed, _ = SRIInformationNeed.objects.get_or_create(
                        id=cityobject,
                        defaults={'descriptioninformationneed': f"Auto-generated for {building_id}"}
                    )
                    # Create a SRIInformationNeedData if it does not exist
                    need_data, _ = SRIInformationNeedData.objects.get_or_create(
                        id=cityobject,
                        defaults={
                            'objectclass': ObjectClass.objects.first(),  # Replace with appropriate objectclass
                            'information_datarequired': infoneed
                        }
                    )
                    instance, created_flag = model.objects.get_or_create(id=need_data)
                elif rel_model.__name__ == 'SRIInformationNeed':
                    # Create a SRIInformationNeed if it does not exist
                    infoneed, _ = SRIInformationNeed.objects.get_or_create(
                        id=cityobject,
                        defaults={'descriptioninformationneed': f"Auto-generated for {building_id}"}
                    )
                    instance, created_flag = model.objects.get_or_create(id=infoneed)
                else:
                    # All other cases: link to CityObject
                    instance, created_flag = model.objects.get_or_create(id=cityobject)
                if created_flag:
                    created.append(f"{model.__name__}")

            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Created the following digital archetypes for building {building_id}: {', '.join(created)}"
                ))
            else:
                self.stdout.write(self.style.NOTICE("No new archetypes were created (all existed)."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to generate digital archetypes: {e}"))
            raise