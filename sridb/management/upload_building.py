from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri import (
    SRISriservice,
    SRIFunctionalitylevel,
    SRISriAssessment,
)
from sridb.management.auxilary.data_cleaning import clean_data , load_building_data


# Class and function to upload a building and its SRI assesment to the database

class Command(BaseCommand):
    help = 'Upload the SRI assesment of a building to the database.'

    def handle(self, path_to_excel_file, *args, **options):
        try:
            # Take the buliding and attach the rating
            df_services = pd.read_excel(path_to_excel_file, sheet_name='Calculation', skiprows=2)
            # clean data
            df_services = clean_data(df_services)

            building_info_df = pd.read_excel(path_to_excel_file, sheet_name='Building info', skiprows=2)
            building_info_dict= load_building_data(building_info_df)


            SRI_building = SRIBuilding.objects.create(id=df_building_info['Building ID'].iloc[0],
                                                      buildingstate = building_info_dict['Building State'],
                                                      sribuildingtype = building_info_dict['Building Type'],
                                                      buildingusage = building_info_dict['Building Usage'],
                                                      climatezone = building_info_dict['Climate Zone'],
                                                      location = building_info_dict['Location'],
                                                      usefulfloorarea = building_info_dict['Useful Floor Area'],
                                                      description = building_info_dict['Description'])

            # Create a new SRI assessment
            # Building , get the ID of a building 

            sri_assessment = SRISriAssessment.objects.create(
                name=df['Building name'].iloc[0],
                score=df['SRI score'].iloc[0],
                date=df['Date'].iloc[0],
            )   

        except Exception as e:
            print(f"Error: {e}")
            raise e



