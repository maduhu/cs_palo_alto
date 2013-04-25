
"""Deletes a firewall rule"""
from baseCmd import *
from baseResponse import *
class deleteFirewallRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the firewall rule"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteFirewallRuleResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

