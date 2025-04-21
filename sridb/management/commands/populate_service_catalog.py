from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri.sri import SRISriservice, SRIFunctionalitylevel, SRIServiceCatalogue
from django.db import transaction
import sys
import os

# Suppress linter warnings for Django's dynamic properties
# pylint: disable=no-member
# flake8: noqa: F821

class Command(BaseCommand):
    help = 'Populates the service catalog with predefined services from an Excel file.'

    # Define the command-line arguments
    def add_arguments(self, parser):
        parser.add_argument('path_to_excel_file', type=str, help='The path to the Excel file containing service definitions.')

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
            default_catalogue, created = SRIServiceCatalogue.objects.get_or_create(
                # Use a unique identifier for the default catalogue
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
                    from sridb.management.auxilary.data_cleaning import clean_data
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

                    # Create or update the service using the code and catalogue as unique identifiers
                    # Note: The 'objects' manager is dynamically added by Django but may trigger linter warnings
                    sriservice, created = SRISriservice.objects.get_or_create(
                        code=service_code,
                        catalogue=default_catalogue,
                        defaults={
                            'domain': row.get('Domain', ''),
                            'impact': row.get('Impact', '0'),
                            'name': row.get('Smart ready service', ''),
                            'partofmethod': row.get('part of the method A: 1 - YES; 0 - NO', 0),
                            'partofmethodb': row.get('part of the method B: 1 - YES; 0 - NO', 0),
                            'preconditions': row.get('Preconditions / Dependency on other services or building types', ''),
                            'servicegroup': row.get('Service group', ''),
                            # Handle potential NaN for userdefined
                            'userdefined': 0 if pd.isna(row.get('part of the custom services list?: 1 - YES; 0 - NO')) 
                                           else int(row.get('part of the custom services list?: 1 - YES; 0 - NO', 0))
                        }
                    )
                    if created:
                         self.stdout.write(f"Created SRISriservice: {sriservice.code}")
                    else:
                         self.stdout.write(f"Found existing SRISriservice: {sriservice.code}")

                    # Define functionality levels
                    functionality_levels_names = ['Functionality level 0 (as non-smart default)',
                                                 'Functionality level 1',
                                                 'Functionality level 2',
                                                 'Functionality level 3',
                                                 'Functionality level 4']
                    
                    # Create functionality levels for this service
                    for functionality_level_num, level_name in enumerate(functionality_levels_names):
                        # Skip if the level description is missing
                        if level_name not in row or pd.isna(row[level_name]):
                             self.stdout.write(f"Skipping {level_name} for service {service_code}: Description missing.")
                             continue

                        level_description = str(row[level_name])
                        level_id_1 = f"{service_code}_{functionality_level_num}" # Create an identifier for the level
                        level_formal_name = f"{row.get('Smart ready service', 'Service')} - {level_name}"

                        # Create or update the functionality level
                        # Note: The 'objects' manager is dynamically added by Django but may trigger linter warnings
                        level_obj, created = SRIFunctionalitylevel.objects.get_or_create(
                            sri_service=sriservice,
                            functionalitylevel=functionality_level_num,
                            defaults={
                                'description': level_description,
                                'id_1': level_id_1,
                                'name': level_formal_name,
                            }
                        )
                        if created:
                            self.stdout.write(f"  Created functionality level {functionality_level_num} for {sriservice.code}")
                        else:
                            self.stdout.write(f"  Updated functionality level {functionality_level_num} for {sriservice.code}")

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
