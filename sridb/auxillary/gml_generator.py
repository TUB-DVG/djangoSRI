from lxml import etree
from sri.pydantic_models import PydanticBuilding

def generate_gml(building: PydanticBuilding) -> str:
    """Generates CityGML from a Pydantic Building Object with Service Data"""
    root = etree.Element("cityModel", attrib={
        "xmlns": "http://www.opengis.net/citygml/2.0",
        "xmlns:sri": "http://www.example.com/sri"
    })

    building_elem = etree.SubElement(root, "bldg:Building", attrib={"gml:id": building.building_id})
    etree.SubElement(building_elem, "Geometry").text = building.geometry

    # SRI Indicator
    if building.sri:
        sri_elem = etree.SubElement(building_elem, "sri:SmartReadinessIndicator")
        for assessment in building.sri.assessments:
            etree.SubElement(sri_elem, "Assessment").text = assessment

    # Energy Systems
    for system in building.energy_systems:
        system_elem = etree.SubElement(building_elem, "EnergySystem", attrib={"type": system.system_type})
        etree.SubElement(system_elem, "EfficiencyScore").text = str(system.efficiency_score)

    # Services
    services_elem = etree.SubElement(building_elem, "sri:Services")
    for service in building.services:
        service_elem = etree.SubElement(services_elem, "sri:Service", attrib={"name": service.name})
        etree.SubElement(service_elem, "TechnicalDomain").text = service.technical_domain
        etree.SubElement(service_elem, "DesiredImpact").text = service.desired_impact

    return etree.tostring(root, pretty_print=True).decode("utf-8")



def generate_gml(building_id):
    building = Building.objects.get(building_id=building_id)
    root = etree.Element("cityModel", attrib={
        "xmlns": "http://www.opengis.net/citygml/2.0",
        "xmlns:sri": "http://www.example.com/sri"
    })
    building_elem = etree.SubElement(root, "bldg:Building", attrib={"gml:id": building.building_id})
    etree.SubElement(building_elem, "Geometry").text = building.geometry
    services_elem = etree.SubElement(building_elem, "sri:MetaServices")
    for service in building.meta_services.all():
        service_elem = etree.SubElement(services_elem, "sri:Service", attrib={"name": service.name})
        etree.SubElement(service_elem, "FunctionalityLevel").text = str(service.functionality_level)
        etree.SubElement(service_elem, "ServiceID").text = service.service_id
        etree.SubElement(service_elem, "Description").text = service.description.description if service.description else "N/A"
    return etree.tostring(root, pretty_print=True).decode("utf-8")
