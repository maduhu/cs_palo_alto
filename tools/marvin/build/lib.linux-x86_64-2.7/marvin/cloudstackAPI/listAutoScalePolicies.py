
"""Lists autoscale policies."""
from baseCmd import *
from baseResponse import *
class listAutoScalePoliciesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """the action to be executed if all the conditions evaluate to true for the specified duration."""
        self.action = None
        """the ID of the condition of the policy"""
        self.conditionid = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """the ID of the autoscale policy"""
        self.id = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the ID of the autoscale vm group"""
        self.vmgroupid = None
        self.required = []

class listAutoScalePoliciesResponse (baseResponse):
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

