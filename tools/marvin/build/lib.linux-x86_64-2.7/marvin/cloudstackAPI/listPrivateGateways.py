
"""List private gateways"""
from baseCmd import *
from baseResponse import *
class listPrivateGatewaysCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        """list only resources belonging to the domain specified"""
        self.domainid = None
        """list private gateway by id"""
        self.id = None
        """list gateways by ip address"""
        self.ipaddress = None
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        """List by keyword"""
        self.keyword = None
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """list objects by project"""
        self.projectid = None
        """list gateways by state"""
        self.state = None
        """list gateways by vlan"""
        self.vlan = None
        """list gateways by vpc"""
        self.vpcid = None
        self.required = []

class listPrivateGatewaysResponse (baseResponse):
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
