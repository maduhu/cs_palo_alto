
"""Deletes an ip forwarding rule"""
from baseCmd import *
from baseResponse import *
class deleteIpForwardingRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the id of the forwarding rule"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteIpForwardingRuleResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

