
"""Creates a vm group"""
from baseCmd import *
from baseResponse import *
class createInstanceGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the name of the instance group"""
        """Required"""
        self.name = None
        """the account of the instance group. The account parameter must be used with the domainId parameter."""
        self.account = None
        """the domain ID of account owning the instance group"""
        self.domainid = None
        """The project of the instance group"""
        self.projectid = None
        self.required = ["name",]

class createInstanceGroupResponse (baseResponse):
    def __init__(self):
        """the id of the instance group"""
        self.id = None
        """the account owning the instance group"""
        self.account = None
        """time and date the instance group was created"""
        self.created = None
        """the domain name of the instance group"""
        self.domain = None
        """the domain ID of the instance group"""
        self.domainid = None
        """the name of the instance group"""
        self.name = None
        """the project name of the group"""
        self.project = None
        """the project id of the group"""
        self.projectid = None

