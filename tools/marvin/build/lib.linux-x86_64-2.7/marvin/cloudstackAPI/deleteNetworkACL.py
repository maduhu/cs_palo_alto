
"""Deletes a Network ACL"""
from baseCmd import *
from baseResponse import *
class deleteNetworkACLCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the network ACL"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteNetworkACLResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

