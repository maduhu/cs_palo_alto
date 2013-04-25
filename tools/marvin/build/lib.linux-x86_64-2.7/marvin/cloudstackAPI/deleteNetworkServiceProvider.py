
"""Deletes a Network Service Provider."""
from baseCmd import *
from baseResponse import *
class deleteNetworkServiceProviderCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the network service provider"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteNetworkServiceProviderResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

