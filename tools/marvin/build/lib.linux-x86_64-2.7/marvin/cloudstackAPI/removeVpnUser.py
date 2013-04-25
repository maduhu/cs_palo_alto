
"""Removes vpn user"""
from baseCmd import *
from baseResponse import *
class removeVpnUserCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """username for the vpn user"""
        """Required"""
        self.username = None
        """an optional account for the vpn user. Must be used with domainId."""
        self.account = None
        """an optional domainId for the vpn user. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """remove vpn user from the project"""
        self.projectid = None
        self.required = ["username",]

class removeVpnUserResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

