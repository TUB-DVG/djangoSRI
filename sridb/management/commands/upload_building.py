from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db import transaction
import pandas as pd
from sridb.modules.sri.sri import (
    SRISriservice,
    SRISriAssessment,
    SRIBuilding,
    SRIServiceCatalogue
)
from sridb.management.auxilary.data_cleaning import load_data, clean_service_data, clean_assessment_data, load_building_data, load_assessment_data
from sridb.management.commands.cityobject import get_or_create_cityobject, get_or_create_building, get_building_by_gml_id, get_service_by_code
import citydb.shortcuts.buildings_data as bldg_short


  

# Class and function to upload a building and its SRI assesment to the database

class Command(BaseCommand):
    help = 'Upload the SRI assessment of a building to the database.'

    def add_arguments(self, parser):
        parser.add_argument('path_to_excel_file', type=str, help='The path to the Excel file containing service definitions.')
        parser.add_argument('building_id', type=str, help='The ID of the building.')

    def handle(self, path_to_excel_file, building_id, *args, **options):
        try:
            # Load and clean building information
            building_info_df = load_data(path_to_excel_file, 'Building Information', 2)          
            building_info_dict = load_building_data(building_info_df)

            # Load and clean assessment information
            building_assessment_df = load_data(path_to_excel_file, 'Calculation', 2)
            building_assessment_df = clean_assessment_data(building_assessment_df)

            # Get or create the building
            building = get_building_by_gml_id(building_id)
            if not building:
                self.stdout.write(self.style.ERROR(f'Building with ID {building_id} not found'))
                return

            # Create or update SRIBuilding
            sri_building_obj, created = SRIBuilding.objects.get_or_create(
                id=building,
                defaults={
                    'buildingstate': building_info_dict['Building State'],
                    'sribuildingtype': building_info_dict['Building Type'],
                    'buildingusage': building_info_dict['Building Usage'],
                    'climatezone': building_info_dict['Climate Zone'],
                    'location': building_info_dict['Location'],
                    'usefulfloorarea': building_info_dict['Useful Floor Area'],
                    'sridescription': building_info_dict['Description']
                }
            )

            # Create a new CityObject for the assessment
            assessment_id = f"SRI_Assessment_{building_id}_{timezone.now().strftime('%Y%m%d_%H%M%S')}"
            assessment_cityobject = get_or_create_cityobject(assessment_id)

            # Create the SRISriAssessment and link it to the building
            with transaction.atomic():
                # First create the assessment
                sri_assessment_obj = SRISriAssessment.objects.create(
                    id=assessment_cityobject,
                    score=12,  # TODO: Calculate actual score
                    dateofassessment=building_info_dict['Date of Assessment']
                )

                # Then save it to ensure it exists in the database
                sri_assessment_obj.save()

                # Now add the building to the M2M relationship
                sri_assessment_obj.buildings.add(sri_building_obj)

                # Process services
                for index, row in building_assessment_df.iterrows():
                    share = row["share (default = 100% means applicable throughout the building)"]
                    if str(share).strip().rstrip('%') not in ('100', '1', '1.0'):
                        self.stdout.write(
                            self.style.WARNING(
                                f'Service with share != 100% found. Share: {share}. Skipping...'
                            )
                        )
                        continue

                    # Get the service code and functionality level
                    code_string = row['Code'] + '_' + str(row['Main functionality level as inspected by SRI assessor '])
                    
                    try:
                        # Get the service and update its properties
                        service_obj = get_service_by_code(code_string)
                        if service_obj:
                            # Create a new service instance for this assessment
                            service_cityobject = get_or_create_cityobject(f"{code_string}_{assessment_id}")
                            new_service = SRISriservice.objects.create(
                                id=service_cityobject,
                                code=service_obj.code,
                                servicename=service_obj.servicename,
                                descriptionfunctionalityleve=service_obj.descriptionfunctionalityleve,
                                functionalitylevel=service_obj.functionalitylevel,
                                impact=service_obj.impact,
                                preconditions=service_obj.preconditions,
                                servicegroup=service_obj.servicegroup,
                                sharefunctionalitylevel=100,  # Convert percentage to integer
                                sridomain=service_obj.sridomain,
                                catalogue=service_obj.catalogue,
                                assessment=sri_assessment_obj
                            )
                        else:
                            self.stdout.write(
                                self.style.WARNING(f'Service with code {code_string} not found. Skipping...')
                            )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f'Error processing service {code_string}: {str(e)}')
                        )
                        continue

            if sri_building_obj and sri_assessment_obj:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully uploaded building {building_id} with SRI assessment')
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to upload building {building_id} or its SRI assessment')
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
            raise e
