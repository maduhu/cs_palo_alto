
"""Lists domains and provides detailed information for listed domains"""
from baseCmd import *
from baseResponse import *
class listDomainsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List domain by domain ID."""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """List domains by domain level."""
        self.level = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """List domain by domain name."""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listDomainsResponse (baseResponse):
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

