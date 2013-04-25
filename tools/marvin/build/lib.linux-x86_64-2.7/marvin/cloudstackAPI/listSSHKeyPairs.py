
"""List registered keypairs"""
from baseCmd import *
from baseResponse import *
class listSSHKeyPairsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """A public key fingerprint to look for"""
        self.fingerprint = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """A key pair name to look for"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list objects by project"""
        self.projectid = None
        self.required = []

class listSSHKeyPairsResponse (baseResponse):
    def __init__(self):
        """Fingerprint of the public key"""
        self.fingerprint = None
        """Name of the keypair"""
        self.name = None
        """Private key"""
        self.privatekey = None

