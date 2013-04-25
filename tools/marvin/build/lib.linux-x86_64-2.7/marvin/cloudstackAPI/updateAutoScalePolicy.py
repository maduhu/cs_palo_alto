
"""Updates an existing autoscale policy."""
from baseCmd import *
from baseResponse import *
class updateAutoScalePolicyCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale policy"""
        """Required"""
        self.id = None
        """the list of IDs of the conditions that are being evaluated on every interval"""
        self.conditionids = []
        """the duration for which the conditions have to be true before action is taken"""
        self.duration = None
        """the cool down period for which the policy should not be evaluated after the action has been taken"""
        self.quiettime = None
        self.required = ["id",]

class updateAutoScalePolicyResponse (baseResponse):
    def __init__(self):
        """the autoscale policy ID"""
        self.id = None
        """the account owning the autoscale policy"""
        self.account = None
        """the action to be executed if all the conditions evaluate to true for the specified duration."""
        self.action = None
        """the list of IDs of the conditions that are being evaluated on every interval"""
        self.conditions = None
        """the domain name of the autoscale policy"""
        self.domain = None
        """the domain ID of the autoscale policy"""
        self.domainid = None
        """the duration for which the conditions have to be true before action is taken"""
        self.duration = None
        """the project name of the autoscale policy"""
        self.project = None
        """the project id autoscale policy"""
        self.projectid = None
        """the cool down period for which the policy should not be evaluated after the action has been taken"""
        self.quiettime = None

