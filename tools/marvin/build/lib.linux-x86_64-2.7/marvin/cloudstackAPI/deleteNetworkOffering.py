
"""Deletes a network offering."""
from baseCmd import *
from baseResponse import *
class deleteNetworkOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the network offering"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteNetworkOfferingResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

