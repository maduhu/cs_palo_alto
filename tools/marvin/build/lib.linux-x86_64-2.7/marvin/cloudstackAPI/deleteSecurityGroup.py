
"""Deletes security group"""
from baseCmd import *
from baseResponse import *
class deleteSecurityGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the account of the security group. Must be specified with domain ID"""
        self.account = None
        """the domain ID of account owning the security group"""
        self.domainid = None
        """The ID of the security group. Mutually exclusive with name parameter"""
        self.id = None
        """The ID of the security group. Mutually exclusive with id parameter"""
        self.name = None
        """the project of the security group"""
        self.projectid = None
        self.required = []

class deleteSecurityGroupResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

