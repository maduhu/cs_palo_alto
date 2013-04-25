
"""Deletes a Private gateway"""
from baseCmd import *
from baseResponse import *
class deletePrivateGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the private gateway"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deletePrivateGatewayResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

