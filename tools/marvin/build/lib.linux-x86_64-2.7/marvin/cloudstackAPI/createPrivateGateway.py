
"""Creates a private gateway"""
from baseCmd import *
from baseResponse import *
class createPrivateGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the gateway of the Private gateway"""
        """Required"""
        self.gateway = None
        """the IP address of the Private gateaway"""
        """Required"""
        self.ipaddress = None
        """the netmask of the Private gateway"""
        """Required"""
        self.netmask = None
        """the Vlan for the private gateway"""
        """Required"""
        self.vlan = None
        """the VPC network belongs to"""
        """Required"""
        self.vpcid = None
        """the Physical Network ID the network belongs to"""
        self.physicalnetworkid = None
        self.required = ["gateway","ipaddress","netmask","vlan","vpcid",]

class createPrivateGatewayResponse (baseResponse):
    def __init__(self):
        """the id of the private gateway"""
        self.id = None
        """the account associated with the private gateway"""
        self.account = None
        """the domain associated with the private gateway"""
        self.domain = None
        """the ID of the domain associated with the private gateway"""
        self.domainid = None
        """the gateway"""
        self.gateway = None
        """the private gateway's ip address"""
        self.ipaddress = None
        """the private gateway's netmask"""
        self.netmask = None
        """the physical network id"""
        self.physicalnetworkid = None
        """the project name of the private gateway"""
        self.project = None
        """the project id of the private gateway"""
        self.projectid = None
        """State of the gateway, can be Creating, Ready, Deleting"""
        self.state = None
        """the vlan of the private gateway"""
        self.vlan = None
        """VPC the private gateaway belongs to"""
        self.vpcid = None
        """zone id of the private gateway"""
        self.zoneid = None
        """the name of the zone the private gateway belongs to"""
        self.zonename = None

