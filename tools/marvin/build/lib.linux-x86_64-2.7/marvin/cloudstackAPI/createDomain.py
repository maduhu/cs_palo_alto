
"""Creates a domain"""
from baseCmd import *
from baseResponse import *
class createDomainCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """creates domain with this name"""
        """Required"""
        self.name = None
        """Network domain for networks in the domain"""
        self.networkdomain = None
        """assigns new domain a parent domain by domain ID of the parent.  If no parent domain is specied, the ROOT domain is assumed."""
        self.parentdomainid = None
        self.required = ["name",]

class createDomainResponse (baseResponse):
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

