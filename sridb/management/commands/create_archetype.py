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
    SRIInformationNeed,
    SRIAssetData,
    SRIIndoorEnvironmentalData,
    SRIControlLogic,
    SRICyberDeviceData,
    SRIDatacategoryMeta,
    SRIEnergyData,
    SRIOperationalData,
    SRIOutdoorenvironmentalData,
    SRIOnsiteenergygeneration,
    SRICyberDeviceData,
    SRIUtilityGridData
)

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
    help = "Import InformationNeed entries from the Excel archetype mapping."

    def add_arguments(self, parser):
        parser.add_argument('gml_id', type=str,
                            help='GML ID of the building to import for')

    def handle(self, *args, **options):
        gml_id = options['gml_id']

        # 1) Resolve building & its services
        building = get_or_create_building(gml_id)
        try:
            sri_building = SRIBuilding.objects.get(id=building)
        except SRIBuilding.DoesNotExist:
            self.stderr.write(f"No SRI building for GML ID {gml_id}")
            return

        services = SRISriservice.objects.filter(building=sri_building)
        if not services:
            self.stderr.write(f"No services found for building {gml_id}")
            return

        # 2) Preload ADE ObjectClass 
        oc_info_need = ObjectClass.objects.get(classname='InformationNeed')

        created = 0
        skipped = 0

        with transaction.atomic():
            for svc in services:
                df = ARCHETYPE_CATALOGUE[
                    (ARCHETYPE_CATALOGUE['FunctionalityLevel'] == svc.functionalitylevel) &
                    (ARCHETYPE_CATALOGUE['Smart ready service'] == svc.servicename)
                ]
                if df.empty:
                    self.stderr.write(
                        f"  • No archetype row for service {svc.servicename!r} @ level {svc.functionalitylevel}"
                    )
                    continue
                row = df.iloc[0]


                # For each info‐need column:
                for col in INFORMATION_NEED_COLUMNS[1:]:
                    cell = row.get(col, '')
                    if not isinstance(cell, str) or ':' not in cell:
                        continue

                    # Split into multiple label:desc by semicolon
                    segments = [seg.strip() for seg in cell.split(';') if ':' in seg]
                    for seg in segments:
                        label, desc = [t.strip() for t in seg.split(':', 1)]
                        SubModel = INFORMATION_NEED_OBJECTS[col]
                        lookup   = build_choice_lookup_for_model(SubModel)
                        field_name, key = lookup.get(label.lower(), (None, None))
                        if not field_name:
                            self.stderr.write(
                                f"    – Unmapped label {label!r} for {SubModel.__name__}"
                            )
                            continue

                        # 3) Create a fresh CityObject for this InformationNeed
                        cityobj = get_or_create_cityobject(
                            f"IN_{svc.id}_{col[:3]}_{label[:3]}"
                        )
                        # 4) Create the base record
                        base = SRIInformationNeed.objects.create(
                            id=cityobj,
                            descriptioninformationneed=desc,
                            objectclass=oc_info_need,
                        )
                        break

                        # 5) Decide if this is a direct subtype or a two-step via SRIDatacategoryMeta
                        parent = SubModel._meta.get_field('id').remote_field.model
                        if parent is SRIDatacategoryMeta:
                            # create the intermediate datacategory row
                            datacat = SRIDatacategoryMeta.objects.create(
                                id=base,
                                datascale=None,
                                other=None
                            )
                            # now the real subtype
                            SubModel.objects.create(id=datacat, **{field_name: key})
                        else:
                            # direct subtype
                            SubModel.objects.create(id=base, **{field_name: key})

                        created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Imported {created} InformationNeed entries "
            f"for building {gml_id}"
        ))