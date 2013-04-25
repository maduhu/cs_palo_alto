
"""Lists all children domains belonging to a specified domain"""
from baseCmd import *
from baseResponse import *
class listDomainChildrenCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list children domain by parent domain ID."""
        self.id = None
        """to return the entire tree, use the value "true". To return the first level children, use the value "false"."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """list children domains by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listDomainChildrenResponse (baseResponse):
    def __init__(self):
        """the ID of the domain"""
        self.id = None
        """whether the domain has one or more sub-domains"""
        self.haschild = None
        """the level of the domain"""
        self.level = None
        """the name of the domain"""
        self.name = None
        """the network domain"""
        self.networkdomain = None
        """the domain ID of the parent domain"""
        self.parentdomainid = None
        """the domain name of the parent domain"""
        self.parentdomainname = None
        """the path of the domain"""
        self.path = None

