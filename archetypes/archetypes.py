from sri.models import Building, SRILevel, EnergySystem

class SRIArchetype:
    def __init__(self, archetype_name, sri_level_name):
        self.archetype_name = archetype_name
        self.sri_level_name = sri_level_name
        self.sri_level = SRILevel.objects.get(level_name=sri_level_name)

    def create_building(self, building_id, geometry):
        building = Building.objects.create(
            building_id=building_id,
            geometry=geometry,
            sri_level=self.sri_level
        )
        return building
