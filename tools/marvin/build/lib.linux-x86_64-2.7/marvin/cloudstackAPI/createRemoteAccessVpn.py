
"""Creates a l2tp/ipsec remote access vpn"""
from baseCmd import *
from baseResponse import *
class createRemoteAccessVpnCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """public ip address id of the vpn server"""
        """Required"""
        self.publicipid = None
        """an optional account for the VPN. Must be used with domainId."""
        self.account = None
        """an optional domainId for the VPN. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        """the range of ip addresses to allocate to vpn clients. The first ip in the range will be taken by the vpn server"""
        self.iprange = None
        """if true, firewall rule for source/end pubic port is automatically created; if false - firewall rule has to be created explicitely. Has value true by default"""
        self.openfirewall = None
        self.required = ["publicipid",]

class createRemoteAccessVpnResponse (baseResponse):
    def __init__(self):
        """the account of the remote access vpn"""
        self.account = None
        """the domain name of the account of the remote access vpn"""
        self.domain = None
        """the domain id of the account of the remote access vpn"""
        self.domainid = None
        """the range of ips to allocate to the clients"""
        self.iprange = None
        """the ipsec preshared key"""
        self.presharedkey = None
        """the project name of the vpn"""
        self.project = None
        """the project id of the vpn"""
        self.projectid = None
        """the public ip address of the vpn server"""
        self.publicip = None
        """the public ip address of the vpn server"""
        self.publicipid = None
        """the state of the rule"""
        self.state = None

