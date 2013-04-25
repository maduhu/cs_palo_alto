
"""Reset site to site vpn connection"""
from baseCmd import *
from baseResponse import *
class resetVpnConnectionCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of vpn connection"""
        """Required"""
        self.id = None
        """an optional account for connection. Must be used with domainId."""
        self.account = None
        """an optional domainId for connection. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.required = ["id",]

class resetVpnConnectionResponse (baseResponse):
    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        """the owner"""
        self.account = None
        """guest cidr list of the customer gateway"""
        self.cidrlist = None
        """the date and time the host was created"""
        self.created = None
        """the domain name of the owner"""
        self.domain = None
        """the domain id of the owner"""
        self.domainid = None
        """if DPD is enabled for customer gateway"""
        self.dpd = None
        """Lifetime of ESP SA of customer gateway"""
        self.esplifetime = None
        """ESP policy of the customer gateway"""
        self.esppolicy = None
        """public ip address id of the customer gateway"""
        self.gateway = None
        """Lifetime of IKE SA of customer gateway"""
        self.ikelifetime = None
        """IKE policy of the customer gateway"""
        self.ikepolicy = None
        """IPsec Preshared-Key of the customer gateway"""
        self.ipsecpsk = None
        """the project name"""
        self.project = None
        """the project id"""
        self.projectid = None
        """the public IP address"""
        self.publicip = None
        """the date and time the host was removed"""
        self.removed = None
        """the customer gateway ID"""
        self.s2scustomergatewayid = None
        """the vpn gateway ID"""
        self.s2svpngatewayid = None
        """State of vpn connection"""
        self.state = None

