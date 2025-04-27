# Function looks up the tag form the parsed xlsx file
from typing import Tuple, Optional

# import or define all your *_tag_choices here
from sridb.modules.sri.information_need import (
    environmentaldatatype_tag_choices,
    scale_tag_choices,
    renewableenergy_tag_choices,
    nonrenewableenergy_tag_choices,
    controlsystem_tag_choices,
    controltype_tag_choices,
    asset_tag_choices,
    enduse_tag_choices,
    energysource_tag_choices,
    systemdata_tag_choices,
    systemtype_tag_choices,
)

# 1) Build one master mapping:
#    maps normalized label → (field_name, internal_key)
LOOKUP: dict[str, Tuple[str, str]] = {}

FIELD_CHOICES = {
    'environmental_data_tag':  environmentaldatatype_tag_choices,
    'scale_tag':               scale_tag_choices,
    'renewable_energy_tag':    renewableenergy_tag_choices,
    'nonrenewable_energy_tag': nonrenewableenergy_tag_choices,
    'control_system_tag':      controlsystem_tag_choices,
    'control_type_tag':        controltype_tag_choices,
    'asset_tag':               asset_tag_choices,
    'enduse_tag':              enduse_tag_choices,
    'energy_source_tag':       energysource_tag_choices,
    'system_data_tag':         systemdata_tag_choices,
    'system_type_tag':         systemtype_tag_choices,
}

for field_name, choices in FIELD_CHOICES.items():
    for key, label in choices:
        LOOKUP[label.strip().lower()] = (field_name, key)


def resolve_tag(label: str) -> Optional[Tuple[str, str]]:
    """
    Given a human‐readable label (e.g. "Non Heated Water"),
    returns (field_name, internal_key), or None if not found.
    """
    return LOOKUP.get(label.strip().lower())
