from lxml import etree
from citydb.modules.bldg.building import Building

def generate_gml(building_pydantic=None, building_id=None):
    """
    Generates CityGML from either a Pydantic Building Object or a Building ID
    
    Args:
        building_pydantic: Optional Pydantic model of a building
        building_id: Optional ID of a building in the database
        
    Returns:
        str: CityGML representation as a string
    """
    # Initialize root element with namespaces
    root = etree.Element("cityModel", attrib={
        "xmlns": "http://www.opengis.net/citygml/2.0",
        "xmlns:bldg": "http://www.opengis.net/citygml/building/2.0",
        "xmlns:gml": "http://www.opengis.net/gml",
        "xmlns:sri": "http://www.example.com/sri"
    })
    
    if building_pydantic:
        # Process Pydantic model
        building_elem = etree.SubElement(root, "bldg:Building", attrib={"gml:id": str(building_pydantic.id)})
        
        # Add geometry if available
        if hasattr(building_pydantic, 'geometry'):
            etree.SubElement(building_elem, "bldg:geometry").text = str(building_pydantic.geometry)
        
        # Add SRI data if available
        if hasattr(building_pydantic, 'sri_data'):
            sri_elem = etree.SubElement(building_elem, "sri:SmartReadinessIndicator")
            
            # Add assessments if available
            if hasattr(building_pydantic, 'sri_assessments'):
                for assessment in building_pydantic.sri_assessments:
                    assessment_elem = etree.SubElement(sri_elem, "sri:Assessment")
                    if hasattr(assessment, 'score'):
                        etree.SubElement(assessment_elem, "sri:Score").text = str(assessment.score)
                    if hasattr(assessment, 'date'):
                        etree.SubElement(assessment_elem, "sri:Date").text = str(assessment.date)
        
        # Add services if available
        if hasattr(building_pydantic, 'services'):
            services_elem = etree.SubElement(building_elem, "sri:Services")
            for service in building_pydantic.services:
                service_elem = etree.SubElement(services_elem, "sri:Service")
                if hasattr(service, 'name'):
                    etree.SubElement(service_elem, "sri:Name").text = service.name
                if hasattr(service, 'domain'):
                    etree.SubElement(service_elem, "sri:Domain").text = service.domain
                if hasattr(service, 'impact'):
                    etree.SubElement(service_elem, "sri:Impact").text = service.impact
                if hasattr(service, 'code'):
                    etree.SubElement(service_elem, "sri:Code").text = service.code
    
    elif building_id:
        # Fetch building from database
        building = Building.objects.get(id=building_id)
        
        # Create building element
        building_elem = etree.SubElement(root, "bldg:Building", attrib={"gml:id": str(building_id)})
        
        # Add SRI building data if available
        try:
            sri_building = building.sribuilding
            if sri_building:
                sri_building_elem = etree.SubElement(building_elem, "sri:SRIBuilding")
                if sri_building.buildingstate:
                    etree.SubElement(sri_building_elem, "sri:BuildingState").text = sri_building.buildingstate
                if sri_building.buildingusage:
                    etree.SubElement(sri_building_elem, "sri:BuildingUsage").text = sri_building.buildingusage
                if sri_building.climatezone:
                    etree.SubElement(sri_building_elem, "sri:ClimateZone").text = sri_building.climatezone
        except:
            pass
        
        # Add SRI services if available
        try:
            services = sri_building.services.all()
            if services:
                services_elem = etree.SubElement(building_elem, "sri:Services")
                for service in services:
                    service_elem = etree.SubElement(services_elem, "sri:Service")
                    if service.name:
                        etree.SubElement(service_elem, "sri:Name").text = service.name
                    if service.domain:
                        etree.SubElement(service_elem, "sri:Domain").text = service.domain
                    if service.impact:
                        etree.SubElement(service_elem, "sri:Impact").text = service.impact
                    if service.code:
                        etree.SubElement(service_elem, "sri:Code").text = service.code
        except:
            pass
    
    # Return the XML as a string
    return etree.tostring(root, pretty_print=True, encoding='utf-8').decode('utf-8')
