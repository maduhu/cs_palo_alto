
"""Register a public key in a keypair under a certain name"""
from baseCmd import *
from baseResponse import *
class registerSSHKeyPairCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Name of the keypair"""
        """Required"""
        self.name = None
        """Public key material of the keypair"""
        """Required"""
        self.publickey = None
        """an optional account for the ssh key. Must be used with domainId."""
        self.account = None
        """an optional domainId for the ssh key. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """an optional project for the ssh key"""
        self.projectid = None
        self.required = ["name","publickey",]

class registerSSHKeyPairResponse (baseResponse):
    def __init__(self):
        """Fingerprint of the public key"""
        self.fingerprint = None
        """Name of the keypair"""
        self.name = None
        """Private key"""
        self.privatekey = None

