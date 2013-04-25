
"""List hypervisors"""
from baseCmd import *
from baseResponse import *
class listHypervisorsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the zone id for listing hypervisors."""
        self.zoneid = None
        self.required = []

class listHypervisorsResponse (baseResponse):
    def __init__(self):
        """Hypervisor name"""
        self.name = None

