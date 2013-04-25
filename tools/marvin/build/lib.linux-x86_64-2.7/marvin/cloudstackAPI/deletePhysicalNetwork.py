
"""Deletes a Physical Network."""
from baseCmd import *
from baseResponse import *
class deletePhysicalNetworkCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the Physical network"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deletePhysicalNetworkResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

