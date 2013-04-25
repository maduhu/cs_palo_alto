
"""Deletes a port forwarding rule"""
from baseCmd import *
from baseResponse import *
class deletePortForwardingRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the port forwarding rule"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deletePortForwardingRuleResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

