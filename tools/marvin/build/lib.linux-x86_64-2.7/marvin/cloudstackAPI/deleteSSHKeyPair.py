
"""Deletes a keypair by name"""
from baseCmd import *
from baseResponse import *
class deleteSSHKeyPairCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Name of the keypair"""
        """Required"""
        self.name = None
        """the account associated with the keypair. Must be used with the domainId parameter."""
        self.account = None
        """the domain ID associated with the keypair"""
        self.domainid = None
        """the project associated with keypair"""
        self.projectid = None
        self.required = ["name",]

class deleteSSHKeyPairResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

