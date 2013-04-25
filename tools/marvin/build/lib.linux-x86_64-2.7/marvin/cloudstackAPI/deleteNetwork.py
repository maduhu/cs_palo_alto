
"""Deletes a network"""
from baseCmd import *
from baseResponse import *
class deleteNetworkCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the network"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteNetworkResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

