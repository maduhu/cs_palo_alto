
"""Deletes network device."""
from baseCmd import *
from baseResponse import *
class deleteNetworkDeviceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Id of network device to delete"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteNetworkDeviceResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

