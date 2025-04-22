from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri.sri import (
    SRISriservice,
    SRIFunctionalitylevel,
    SRISriAssessment,
    SRIBuilding
)
from sridb.management.auxilary.data_cleaning import clean_data , load_building_data
from sridb.management.commands.cityobject import get_or_create_cityobject, get_or_create_building, get_building_by_gml_id
import citydb.shortcuts.buildings_data as bldg_short


  

# Class and function to upload a building and its SRI assesment to the database

class Command(BaseCommand):
    help = 'Upload the SRI assesment of a building to the database.'

    def add_arguments(self, parser):
        parser.add_argument('path_to_excel_file', type=str, help='The path to the Excel file containing service definitions.')
        parser.add_argument('building_id', type=str, help='The ID of the building.')

    def handle(self, path_to_excel_file, building_id, *args, **options):
        try:
                # Try different engines if one fails
            try:
                building_info_df = pd.read_excel(path_to_excel_file, sheet_name='Building Information', engine='openpyxl', skiprows=2)
            except Exception as e:
                self.stdout.write(f"Failed with openpyxl engine: {e}")
                try:
                    building_info_df = pd.read_excel(path_to_excel_file, sheet_name='Building Information', engine='xlrd', skiprows=2)
                except Exception as e2:
                    self.stdout.write(f"Failed with xlrd engine: {e2}")
                    # Last resort
                    building_info_df = pd.read_excel(path_to_excel_file, sheet_name='Building Information', skiprows=2)
            
            building_info_dict= load_building_data(building_info_df)


            building = get_building_by_gml_id(building_id)


            SRI_building, created = SRIBuilding.objects.get_or_create(id=building,
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

            sri_assessment, created = SRISriAssessment.objects.get_or_create(
                                            defaults={
                                            'score': 12,
                                            'dateofassessment': building_info_dict['Date of Assessment'],
                                            })

            ## Attach the assessment to the building
            #SRI_building.assessments.add(sri_assessment)



        except Exception as e:
            print(f"Error: {e}")
            raise e



