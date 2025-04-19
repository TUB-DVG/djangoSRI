from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from sridb.modules.sri import (
    SRISriservice,
    SRIFunctionalitylevel
)

class Command(BaseCommand):
    help = 'Create an archetype'

    def handle(self, *args, **options):
        pass

        # Class and function to create an archetype
        # building based on a mapping of attributes
