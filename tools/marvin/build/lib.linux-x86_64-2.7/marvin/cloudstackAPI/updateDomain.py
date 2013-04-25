
"""Updates a domain with a new name"""
from baseCmd import *
from baseResponse import *
class updateDomainCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """ID of domain to update"""
        """Required"""
        self.id = None
        """updates domain with this name"""
        self.name = None
        """Network domain for the domain's networks; empty string will update domainName with NULL value"""
        self.networkdomain = None
        self.required = ["id",]

class updateDomainResponse (baseResponse):
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

