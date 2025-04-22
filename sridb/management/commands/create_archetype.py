from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri import (
    SRISriservice,
    SRIFunctionalitylevel
)
from sridb.management.commands.cityobject import get_building_by_gml_id

class Command(BaseCommand):
    help = 'Create an archetype'

    def add_arguments(self, parser):
        parser.add_argument('gml_id', type=str, help='The GML ID of the building to create an archetype for')

    def handle(self, *args, **options):
        # Get the building by id 
         building = get_building_by_gml_id(options['gml_id'])
        # Class and function to create an archetype
        # building based on a mapping of attributes
        services = SRISriservice.objects.filter(catalogue=building.sriservices)
        # Create a dictionary of services
        for service in services:
            print(service.name)

   