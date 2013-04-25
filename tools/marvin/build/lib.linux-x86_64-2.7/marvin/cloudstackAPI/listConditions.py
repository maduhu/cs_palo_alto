
"""List Conditions for the specific user"""
from baseCmd import *
from baseResponse import *
class listConditionsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """Counter-id of the condition."""
        self.counterid = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """ID of the Condition."""
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
        """the ID of the policy"""
        self.policyid = None
        self.required = []

class listConditionsResponse (baseResponse):
    def __init__(self):
        """the id of the Counter"""
        self.id = None
        """Name of the counter."""
        self.name = None
        """Source of the counter."""
        self.source = None
        """Value in case of snmp or other specific counters."""
        self.value = None
        """zone id of counter"""
        self.zoneid = None

