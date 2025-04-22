from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from citydb.models import CityObject
from citydb.modules.core.objectclass import ObjectClass
from citydb.modules.bldg.building import Building
from sridb.management.auxilary.data_cleaning import clean_data , load_building_data





def get_or_create_cityobject(cityobject_id: int) -> CityObject:
    """
    Get or create a CityObject instance based on the provided ID.

    This function checks if a CityObject with the given ID exists in the database.
    """
    objclass = ObjectClass.objects.get(classname='Building')
    cityobject, created = CityObject.objects.get_or_create(gmlid=cityobject_id,
                                                           defaults={'objectclass': objclass,})
    return cityobject



def get_or_create_building(gmlid: str) -> Building:
    cityobj, _ = CityObject.objects.get_or_create(
        gmlid=gmlid,
        defaults={
            'objectclass': ObjectClass.objects.get(classname='Building'),  
        }
    )

    # Building doesn't have objects manager directly, need to access through cityobj
    # The Building model is linked to CityObject via a OneToOneField
    building = None
    if cityobj:
        try:
            # Access the building through the cityobj relationship
            building = cityobj.building_obj
            print(f"Found building with gmlid: {gmlid}")
        except Building.DoesNotExist:
            print(f"No building found with gmlid: {gmlid}")
    
    if not building:
        print(f"Creating new building for gmlid: {gmlid}")
        #building = Building.objects.create(_parent_link=cityobj)
    return  Building.objects.get(gmlid=gmlid)

def get_building_by_gml_id(gml_id):
    """
    Get a building by its GML ID from a specific city model.
    
    This function filters CityObjects that belong to the given city model,
    are of type Building, and have the specified GML ID.
    """
    building = Building.objects.filter(gmlid=gml_id)
    if not building:
        raise ValueError(f"No building found with gmlid: {gml_id}")
    return building[0]
