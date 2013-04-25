
"""Creates site to site vpn customer gateway"""
from baseCmd import *
from baseResponse import *
class createVpnCustomerGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """guest cidr list of the customer gateway"""
        """Required"""
        self.cidrlist = None
        """ESP policy of the customer gateway"""
        """Required"""
        self.esppolicy = None
        """public ip address id of the customer gateway"""
        """Required"""
        self.gateway = None
        """IKE policy of the customer gateway"""
        """Required"""
        self.ikepolicy = None
        """IPsec Preshared-Key of the customer gateway"""
        """Required"""
        self.ipsecpsk = None
        """the account associated with the gateway. Must be used with the domainId parameter."""
        self.account = None
        """the domain ID associated with the gateway. If used with the account parameter returns the gateway associated with the account for the specified domain."""
        self.domainid = None
        """If DPD is enabled for VPN connection"""
        self.dpd = None
        """Lifetime of phase 2 VPN connection to the customer gateway, in seconds"""
        self.esplifetime = None
        """Lifetime of phase 1 VPN connection to the customer gateway, in seconds"""
        self.ikelifetime = None
        """name of this customer gateway"""
        self.name = None
        self.required = ["cidrlist","esppolicy","gateway","ikepolicy","ipsecpsk",]

class createVpnCustomerGatewayResponse (baseResponse):
    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        """the owner"""
        self.account = None
        """guest cidr list of the customer gateway"""
        self.cidrlist = None
        """the domain name of the owner"""
        self.domain = None
        """the domain id of the owner"""
        self.domainid = None
        """if DPD is enabled for customer gateway"""
        self.dpd = None
        """Lifetime of ESP SA of customer gateway"""
        self.esplifetime = None
        """IPsec policy of customer gateway"""
        self.esppolicy = None
        """public ip address id of the customer gateway"""
        self.gateway = None
        """Lifetime of IKE SA of customer gateway"""
        self.ikelifetime = None
        """IKE policy of customer gateway"""
        self.ikepolicy = None
        """guest ip of the customer gateway"""
        self.ipaddress = None
        """IPsec preshared-key of customer gateway"""
        self.ipsecpsk = None
        """name of the customer gateway"""
        self.name = None
        """the project name"""
        self.project = None
        """the project id"""
        self.projectid = None
        """the date and time the host was removed"""
        self.removed = None

