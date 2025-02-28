from sri.models import Service, FunctionalityLevel, ServiceGroup

def create_heating_services():
    """Create predefined heating services from the standard"""
    
    # Heat control - demand side group
    heat_control_group = ServiceGroup.objects.create(
        name="Heat control - demand side",
        technical_domain="heating",
        code="H-1"
    )

    # H1a - Heat emission control
    h1a = Service.objects.create(
        name="Heat emission control",
        service_id="H1a",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=True,
        part_b=True,
        triage_score=0
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h1a, level=0, description="No automatic control", is_non_smart_default=True),
        FunctionalityLevel(service=h1a, level=1, description="Central automatic control (e.g. central thermostat)"),
        FunctionalityLevel(service=h1a, level=2, description="Individual room control (e.g. thermostatic valves, or electronic controller)"),
        FunctionalityLevel(service=h1a, level=3, description="Individual room control with communication between controllers and to BACS"),
        FunctionalityLevel(service=h1a, level=4, description="Individual room control with communication and occupancy detection")
    ])

    # H1b - Emission control for TABS
    h1b = Service.objects.create(
        name="Emission control for TABS (heating mode)",
        service_id="H1b",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=False,
        part_b=True,
        triage_score=0,
        preconditions="Triage: not relevant in case of TABS. Mostly restricted to non-residential buildings"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h1b, level=0, description="No automatic control", is_non_smart_default=True),
        FunctionalityLevel(service=h1b, level=1, description="Central automatic control"),
        FunctionalityLevel(service=h1b, level=2, description="Advanced central automatic control"),
        FunctionalityLevel(service=h1b, level=3, description="Advanced central automatic control with intermittent operation and/or room temperature feedback control"),
        FunctionalityLevel(service=h1b, level=4, description="Advanced central automatic control with intermittent operation and/or room temperature feedback control")
    ])

    # H1c - Control of distribution fluid temperature
    h1c = Service.objects.create(
        name="Control of distribution fluid temperature (supply or return air flow or water flow)",
        service_id="H1c",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=True,
        part_b=True,
        triage_score=0,
        preconditions="Not applicable in case of individual heaters (e.g. stoves)"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h1c, level=0, description="No automatic control", is_non_smart_default=True),
        FunctionalityLevel(service=h1c, level=1, description="Outside temperature compensated control"),
        FunctionalityLevel(service=h1c, level=2, description="Demand based control"),
    ])

    # H1d - Control of distribution pumps
    h1d = Service.objects.create(
        name="Control of distribution pumps in networks",
        service_id="H1d",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=False,
        part_b=True,
        triage_score=0,
        preconditions="Only applicable for hydronic heating systems"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h1d, level=0, description="No automatic control", is_non_smart_default=True),
        FunctionalityLevel(service=h1d, level=1, description="On/off control"),
        FunctionalityLevel(service=h1d, level=2, description="Multi-stage control"),
        FunctionalityLevel(service=h1d, level=3, description="Variable speed pump control (pump and pressure difference)"),
        FunctionalityLevel(service=h1d, level=4, description="Variable speed pump control (demand evaluation)")
    ])

    # H1f - Thermal Energy Storage (TES) control
    h1f = Service.objects.create(
        name="Thermal Energy Storage (TES) for building heating (excluding TABS)",
        service_id="H1f",
        technical_domain="heating",
        desired_impact="energy_flexibility_storage",
        part_a=False,
        part_b=True,
        triage_score=0,
        preconditions="Only applicable in case thermal energy storage is present"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h1f, level=0, description="Continuous storage operation", is_non_smart_default=True),
        FunctionalityLevel(service=h1f, level=1, description="Time-scheduled storage operation"),
        FunctionalityLevel(service=h1f, level=2, description="Load prediction based storage operation"),
        FunctionalityLevel(service=h1f, level=3, description="Heat storage capable of flexible control through grid signals (e.g. DSM)")
    ])

    # Control heat production facilities group
    heat_prod_group = ServiceGroup.objects.create(
        name="Control heat production facilities",
        technical_domain="heating",
        code="H-2"
    )

    # H2a - Heat generator control (all except heat pumps)
    h2a = Service.objects.create(
        name="Heat generator control (all except heat pumps)",
        service_id="H2a",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=True,
        part_b=True,
        triage_score=0,
        preconditions="Only applicable in case of combustion/district heating"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h2a, level=0, description="Constant temperature control", is_non_smart_default=True),
        FunctionalityLevel(service=h2a, level=1, description="Variable temperature control depending on outdoor temperature"),
        FunctionalityLevel(service=h2a, level=2, description="Variable temperature control depending on the load (e.g. depending on supply water temperature set point)")
    ])

    # H2b - Heat generator control (for heat pumps)
    h2b = Service.objects.create(
        name="Heat generator control (for heat pumps)",
        service_id="H2b",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=True,
        part_b=True,
        triage_score=0,
        preconditions="Only applicable in case of heat pumps"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h2b, level=0, description="On/Off control of heat generator", is_non_smart_default=True),
        FunctionalityLevel(service=h2b, level=1, description="Multi-stage control of heat generator capacity depending on the load or demand (e.g. on/off of several compressors)"),
        FunctionalityLevel(service=h2b, level=2, description="Variable control of heat generator capacity depending on the load or demand (e.g. hot gas bypass, inverter frequency control)"),
        FunctionalityLevel(service=h2b, level=3, description="Variable control of heat generator capacity depending on the load AND external signals from grid")
    ])

    # H2d - Sequencing of different heat generators
    h2d = Service.objects.create(
        name="Sequencing in case of different heat generators",
        service_id="H2d",
        technical_domain="heating",
        desired_impact="energy_efficiency",
        part_a=False,
        part_b=True,
        triage_score=0,
        preconditions="Only applicable in case of multiple heat generators"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h2d, level=0, description="Priorities only based on running time", is_non_smart_default=True),
        FunctionalityLevel(service=h2d, level=1, description="Control according to fixed priority list (e.g. based on rated energy efficiency)"),
        FunctionalityLevel(service=h2d, level=2, description="Control according to dynamic priority list (based on current energy efficiency, carbon emissions and capacity of generators)"),
        FunctionalityLevel(service=h2d, level=3, description="Control according to dynamic priority list (based on current AND predicted load, energy efficiency, carbon emissions, capacity of generators)"),
        FunctionalityLevel(service=h2d, level=4, description="Control according to dynamic priority list (based on current AND predicted load, energy efficiency, carbon emissions, capacity of generators AND external signals from grid)")
    ])

    # Information to occupants group
    info_group = ServiceGroup.objects.create(
        name="Information to occupants and facility managers",
        technical_domain="heating",
        code="H-3"
    )

    # H3 - Reporting information
    h3 = Service.objects.create(
        name="Report information regarding heating system performance",
        service_id="H3",
        technical_domain="heating",
        desired_impact="information_to_occupants",
        part_a=True,
        part_b=True,
        triage_score=1
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h3, level=0, description="None", is_non_smart_default=True),
        FunctionalityLevel(service=h3, level=1, description="Central or remote reporting of current performance KPIs (e.g. temperatures, submetering energy usage)"),
        FunctionalityLevel(service=h3, level=2, description="Central or remote reporting of performance evaluation including forecasting and/or benchmarking"),
        FunctionalityLevel(service=h3, level=3, description="Central or remote reporting of performance evaluation including forecasting and/or benchmarking; also including predictive maintenance")
    ])

    # H4 - Flexibility and grid interaction
    h4 = Service.objects.create(
        name="Flexibility and grid interaction",
        service_id="H4",
        technical_domain="heating",
        desired_impact="energy_flexibility_storage",
        part_a=False,
        part_b=True,
        triage_score=1,
        preconditions="The inspectability of the nature of the control algorithm would need to be facilitated"
    )
    
    FunctionalityLevel.objects.bulk_create([
        FunctionalityLevel(service=h4, level=0, description="No automatic control", is_non_smart_default=True),
        FunctionalityLevel(service=h4, level=1, description="Scheduled operation of heating system"),
        FunctionalityLevel(service=h4, level=2, description="Self-learning optimal control of heating system"),
        FunctionalityLevel(service=h4, level=3, description="Heating system capable of flexible control through grid signals (e.g. through model predictive control)")
    ])
