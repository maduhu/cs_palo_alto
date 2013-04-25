
"""Deletes a load balancer rule."""
from baseCmd import *
from baseResponse import *
class deleteLoadBalancerRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the load balancer rule"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteLoadBalancerRuleResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

