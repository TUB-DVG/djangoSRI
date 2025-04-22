from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import IntegrityError
import pandas as pd
from sridb.modules.sri.sri import SRISriservice, SRIFunctionalitylevel, SRIServiceCatalogue
from django.db import transaction
import sys
import os
from sridb.management.commands.cityobject import get_or_create_cityobject, get_building_by_gml_id
from citydb.modules.core.objectclass import ObjectClass
from citydb.models import CityObject
from sridb.management.auxilary.data_cleaning import clean_data

# Suppress linter warnings for Django's dynamic properties
# pylint: disable=no-member
# flake8: noqa: F821

class Command(BaseCommand):
    help = 'Populates the service catalog with predefined services from an Excel file.'

    # Define the command-line arguments
    def add_arguments(self, parser):
        parser.add_argument('path_to_excel_file', type=str, help='The path to the Excel file containing service definitions.')
        parser.add_argument('building_id', type=str, help='The GML ID of the building to which the service catalog belongs.')

    def handle(self, *args, **options):
        # Get the file path from the options dictionary
        path_to_excel_file = options['path_to_excel_file']
        
        self.stdout.write(f"Starting service catalog population from: {path_to_excel_file}")
        
        # Check Python version
        self.stdout.write(f"Using Python version: {sys.version}")
        
        # Wrap all database operations in a transaction
        with transaction.atomic():
            # Create or get the default service catalog
            # Note: The 'objects' manager is dynamically added by Django but may trigger linter warnings
            building = get_building_by_gml_id(options['building_id'])
            
            # Get or create CityObject for the service catalogue
            #obj_class = ObjectClass.objects.get(classname='SRIServiceCatalogue')
            #cat_cityobj = get_or_create_cityobject(f"SRI_Catalog_{building.gmlid}")
            #cat_cityobj.objectclass = obj_class
            #cat_cityobj.save()
            
            default_catalogue, created = SRIServiceCatalogue.objects.get_or_create(
                # Use a unique identifier for the default catalogue
                id = building,
                version=1.0,
                defaults={
                    'description': "Default Service Catalogue populated from Excel",
                }
            )
            
            if created:
                self.stdout.write(f"Created new default service catalogue with ID: {default_catalogue.id}")
            else:
                self.stdout.write(f"Using existing default service catalogue with ID: {default_catalogue.id}")
            
            try:
                # Check if file exists before attempting to read
                if not os.path.exists(path_to_excel_file):
                    raise FileNotFoundError(f"File not found: {path_to_excel_file}")
                    
                # Try different engines if one fails
                try:
                    df = pd.read_excel(path_to_excel_file, sheet_name='overview_of_services', engine='openpyxl')
                except Exception as e:
                    self.stdout.write(f"Failed with openpyxl engine: {e}")
                    try:
                        df = pd.read_excel(path_to_excel_file, sheet_name='overview_of_services', engine='xlrd')
                    except Exception as e2:
                        self.stdout.write(f"Failed with xlrd engine: {e2}")
                        # Last resort
                        df = pd.read_excel(path_to_excel_file, sheet_name='overview_of_services')
                
                # Clean data if the function is available
                try:
                    df = clean_data(df)
                except ImportError:
                    self.stdout.write("Data cleaning module not found, proceeding with raw data")
                
                # Process each service from the Excel file
                for index, row in df.iterrows():
                    # Ensure required columns exist and handle potential NaN in code
                    if 'Code' not in row or pd.isna(row['Code']):
                        self.stdout.write(f"Skipping row {index} due to missing or invalid 'Code'.")
                        continue
                    
                    service_code = str(row['Code']) # Ensure code is string

                    # Create or update the service using the code and catalogue as unique identifier
                    # Define functionality levels
                    functionality_levels_names = ['Functionality level 0 (as non-smart default)',
                                                 'Functionality level 1',
                                                 'Functionality level 2',
                                                 'Functionality level 3',
                                                 'Functionality level 4']
                    
                    # Create functionality levels for this service
                    for functionality_level_num, level_name in enumerate(functionality_levels_names):
                        # Skip if the level description is missing
                        
                        level_description = str(row[level_name])
                        level_formal_name = f"{row.get('Smart ready service', 'Service')} - {level_name}"

                        # Create or update the functionality level
                        # Note: The 'objects' manager is dynamically added by Django but may trigger linter warnings
                        try:
                            # Create or update the service using the code and catalogue as unique identifier
                            sriservice, created = SRISriservice.objects.get_or_create(
                                code=service_code + '_' + str(functionality_level_num),
                                catalogue=default_catalogue,
                                defaults={
                                'sridomain': row.get('Domain', 'Other'),
                                'name': row.get('Smart ready service', ''),
                                'partofmethod': row.get('part of the method A: 1 - YES; 0 - NO', 0),
                                'partofmethodb': row.get('part of the method B: 1 - YES; 0 - NO', 0),
                                'preconditions': row.get('Preconditions / Dependency on other services or building types', ''),
                                'servicegroup': row.get('Service group', ''),
                                'functionalitylevel': functionality_level_num,
                                'descriptionfunctionalityleve': level_description,
                                'sharefunctionalitylevel': row.get('Share of functionality level', 0),
                                # Handle potential NaN for userdefined
                                'userdefined': 0 if pd.isna(row.get('part of the custom services list?: 1 - YES; 0 - NO')) 
                                                else int(row.get('part of the custom services list?: 1 - YES; 0 - NO', 0))
                                }
                            )
                        except IntegrityError as e:
                            self.stdout.write(f"  IntegrityError: {e}")
                            continue
                        if created:
                            self.stdout.write(f"Created functionality level {functionality_level_num} for {sriservice.code}")
                        else:
                            # ToDo: Write update functionality
                            self.stdout.write(f"Service {sriservice.code} with functionality level {functionality_level_num} already exists - skipping")

                # style.SUCCESS is a property dynamically added by Django's BaseCommand
                self.stdout.write(self.style.SUCCESS('Successfully populated service catalog.'))

            except FileNotFoundError:
                # style.ERROR is a property dynamically added by Django's BaseCommand
                self.stderr.write(self.style.ERROR(f"Error: File not found at {path_to_excel_file}"))
            except Exception as e:
                # style.ERROR is a property dynamically added by Django's BaseCommand
                self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
                # Reraise the exception to see the full traceback if needed
                raise e
