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
from sridb.management.auxilary.data_cleaning import load_data, clean_service_data , clean_assessment_data, load_building_data, load_assessment_data
from sridb.management.commands.cityobject import get_or_create_cityobject, get_or_create_building, get_building_by_gml_id, get_service_by_code
import citydb.shortcuts.buildings_data as bldg_short


  

# Class and function to upload a building and its SRI assesment to the database

class Command(BaseCommand):
    help = 'Upload the SRI assesment of a building to the database.'

    def add_arguments(self, parser):
        parser.add_argument('path_to_excel_file', type=str, help='The path to the Excel file containing service definitions.')
        parser.add_argument('building_id', type=str, help='The ID of the building.')

    def handle(self, path_to_excel_file, building_id, *args, **options):
        try:
            building_info_df = load_data(path_to_excel_file, 'Building Information', 2)          
            building_info_dict= load_building_data(building_info_df)

            building_assesment_df = load_data(path_to_excel_file, 'Calculation', 2)
            building_assesment_df = clean_assessment_data(building_assesment_df)
            #assessment_info_dict = load_assessment_data(building_assesment_df)


            building = get_building_by_gml_id(building_id)


            sri_building_obj, created = SRIBuilding.objects.get_or_create(id=building,
                                                      defaults={
                                                      'buildingstate': building_info_dict['Building State'],
                                                      'sribuildingtype': building_info_dict['Building Type'],
                                                      'buildingusage': building_info_dict['Building Usage'],
                                                      'climatezone': building_info_dict['Climate Zone'],
                                                      'location': building_info_dict['Location'],
                                                      'usefulfloorarea': building_info_dict['Useful Floor Area'],
                                                      'sridescription': building_info_dict['Description']
                                                      })

            # Create a new SRI assessment
            # Use the SRI building and attach the Assessment
            
            
            cityobject = get_or_create_cityobject(sri_building_obj.id)
            sri_assessment_obj, created = SRISriAssessment.objects.get_or_create(
                                            defaults={
                                            #'assessor_id': building_info_dict['Assessor Name'],
                                            'score': 12,
                                            'dateofassessment': building_info_dict['Date of Assessment'],
                                            })
            # Add the Assessor to the assessment

            ## Attach the assessment to the building
            #SRI_building.assessments.add(sri_assessment)
            with transaction.atomic():
                for index, row in building_assesment_df.iterrows():
                    # Check level
                    # Check share of level
                    # Get level 
                    # How to deal with comment from the assessment?
                    share = row["share (default = 100% means applicable throughout the building)"]
                    if str(share).strip().rstrip('%') not in ('100', '1', '1.0'):
                        self.stdout.write(self.style.ERROR(f'Failed to upload building {building_id} or its SRI assessment. Share is not 100%'))
                        continue
                    else:
                        # Note in version 4.5 the functionality level is called 'Main functionality level as inspected by SRI assessor '
                        #  Note the space at the end of the column name
                        code_string = row['Code'] + '_' + str(row['Main functionality level as inspected by SRI assessor '])
                        # Create or update the service link (junction model)
                        service_obj = get_service_by_code(code_string)
                        service_obj.sharefunctionalitylevel = share
                        service_obj.building = sri_building_obj
                        service_obj.save()
                        #
                        #obj, created = SRISriservice.objects.update_or_create(building=sri_building_obj, 
                        #                 defaults={
                        #                    'sharefunctionalitylevel': share,
                        #                    #'comment': row['Comment']
                        #                })
                        #    #sri_services_obj = get_service_by_code(code_string)
                        #    #print(sri_services_obj)
                        #    #sri_assessment_obj.services.add(sri_services_obj)
                        #    #sri_building_obj.services.add(sri_services_obj)


            if sri_building_obj and sri_assessment_obj:
                self.stdout.write(self.style.SUCCESS(f'Successfully uploaded building {building_id} with SRI assessment'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to upload building {building_id} or its SRI assessment'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
            raise e
