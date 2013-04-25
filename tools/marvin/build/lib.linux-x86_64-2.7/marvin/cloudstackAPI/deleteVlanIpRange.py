
"""Creates a VLAN IP range."""
from baseCmd import *
from baseResponse import *
class deleteVlanIpRangeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the id of the VLAN IP range"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVlanIpRangeResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

