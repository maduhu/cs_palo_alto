
"""Configures a virtual router element."""
from baseCmd import *
from baseResponse import *
class configureVirtualRouterElementCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the virtual router provider"""
        """Required"""
        self.id = None
        """Enabled/Disabled the service provider"""
        """Required"""
        self.enabled = None
        self.required = ["id","enabled",]

class configureVirtualRouterElementResponse (baseResponse):
    def __init__(self):
        """the id of the router"""
        self.id = None
        """the account associated with the provider"""
        self.account = None
        """the domain associated with the provider"""
        self.domain = None
        """the domain ID associated with the provider"""
        self.domainid = None
        """Enabled/Disabled the service provider"""
        self.enabled = None
        """the physical network service provider id of the provider"""
        self.nspid = None
        """the project name of the address"""
        self.project = None
        """the project id of the ipaddress"""
        self.projectid = None
