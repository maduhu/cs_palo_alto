
"""Removes a virtual machine or a list of virtual machines from a load balancer rule."""
from baseCmd import *
from baseResponse import *
class removeFromLoadBalancerRuleCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """The ID of the load balancer rule"""
        """Required"""
        self.id = None
        """the list of IDs of the virtual machines that are being removed from the load balancer rule (i.e. virtualMachineIds=1,2,3)"""
        """Required"""
        self.virtualmachineids = []
        self.required = ["id","virtualmachineids",]

class removeFromLoadBalancerRuleResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

