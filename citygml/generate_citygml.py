from lxml import etree
from sri.models import Building

def generate_citygml(building_id):
    building = Building.objects.get(building_id=building_id)
    
    root = etree.Element("cityModel", attrib={
        "xmlns": "http://www.opengis.net/citygml/2.0",
        "xmlns:sri": "http://www.example.com/sri"
    })

    building_elem = etree.SubElement(root, "bldg:Building", attrib={"gml:id": building.building_id})
    etree.SubElement(building_elem, "sri:SmartReadinessIndicator").text = building.sri_level.level_name

    return etree.tostring(root, pretty_print=True).decode("utf-8")
