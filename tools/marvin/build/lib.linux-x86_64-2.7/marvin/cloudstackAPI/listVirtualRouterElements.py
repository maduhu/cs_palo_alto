
"""Lists all available virtual router elements."""
from baseCmd import *
from baseResponse import *
class listVirtualRouterElementsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list network offerings by enabled state"""
        self.enabled = None
        """list virtual router elements by id"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """list virtual router elements by network service provider id"""
        self.nspid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listVirtualRouterElementsResponse (baseResponse):
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

