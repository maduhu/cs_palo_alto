
"""Adds vpn users"""
from baseCmd import *
from baseResponse import *
class addVpnUserCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """password for the username"""
        """Required"""
        self.password = None
        """username for the vpn user"""
        """Required"""
        self.username = None
        """an optional account for the vpn user. Must be used with domainId."""
        self.account = None
        """an optional domainId for the vpn user. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """add vpn user to the specific project"""
        self.projectid = None
        self.required = ["password","username",]

class addVpnUserResponse (baseResponse):
    def __init__(self):
        """the vpn userID"""
        self.id = None
        """the account of the remote access vpn"""
        self.account = None
        """the domain name of the account of the remote access vpn"""
        self.domain = None
        """the domain id of the account of the remote access vpn"""
        self.domainid = None
        """the project name of the vpn"""
        self.project = None
        """the project id of the vpn"""
        self.projectid = None
        """the username of the vpn user"""
        self.username = None

