
"""Creates site to site vpn local gateway"""
from baseCmd import *
from baseResponse import *
class createVpnGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """public ip address id of the vpn gateway"""
        """Required"""
        self.vpcid = None
        self.required = ["vpcid",]

class createVpnGatewayResponse (baseResponse):
    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        """the owner"""
        self.account = None
        """the domain name of the owner"""
        self.domain = None
        """the domain id of the owner"""
        self.domainid = None
        """the project name"""
        self.project = None
        """the project id"""
        self.projectid = None
        """the public IP address"""
        self.publicip = None
        """the date and time the host was removed"""
        self.removed = None
        """the vpc id of this gateway"""
        self.vpcid = None

