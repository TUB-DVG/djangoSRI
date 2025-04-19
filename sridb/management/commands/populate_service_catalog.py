from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri import (
    SRISriservice,
    SRIFunctionalitylevel
)
from sridb.management.auxilary.data_cleaning import clean_data




class Command(BaseCommand):
    help = 'Populates the service catalog with predefined services'

    def handle(self, path_to_excel_file, *args, **options):
        # Create or get the service catalog
        catalog, _ = ServiceCatalog.objects.get_or_create(
            name="Smart Readiness Indicator Standard Catalog",
            version="4.5",
            defaults={
                'publication_date': timezone.now().date(),
                'description': "Standard service catalog for SRI assessment"
            }
        )
        try:
            df = pd.read_excel(path_to_excel_file, sheet_name='overview_of_services')
            df = clean_data(df)
            # Create service groups
            for index, row in df.iterrows():
                # Create a smart ready service
                sriservice, _ = SRISriservice.objects.get_or_create(
                    code=row['Code'],
                    domain=row['Domain'],
                    impact=row['Impact'],
                    name=row['Service ready service'],
                    partofmethod=row['part of the method A: 1 - YES; 0 - NO'],
                    partofmethodb=row['part of the method B: 1 - YES; 0 - NO'],
                    preconditions=row['Preconditions / Dependency on other services or building types'],
                    servicegroup=row['Service group'],
                    userdefined=row['part of the custom services list?: 1 - YES; 0 - NO']
                )
                # Check amount of functionality levels
                functionality_levels = ['Functionality level 0 (as non-smart default)',
                                        'Functionality level 1',
                                        'Functionality level 2',
                                        'Functionality level 3',
                                        'Functionality level 4']
                for functionality_level, i in enumerate(functionality_levels):
                    SRIFunctionalitylevel.objects.get_or_create(
                        description=row[i],
                        functionalitylevel=i,
                        id_1=row["Code"] + "_" + i,
                        name=row["Service ready service"] + " - " + i,
                        sriservice=sriservice
                    )

        except Exception as e:
            print(f"Error: {e}")
            raise e

