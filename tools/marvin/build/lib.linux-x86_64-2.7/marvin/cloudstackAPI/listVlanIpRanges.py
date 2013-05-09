
"""Lists all VLAN IP ranges."""
from baseCmd import *
from baseResponse import *
class listVlanIpRangesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the account with which the VLAN IP range is associated. Must be used with the domainId parameter."""
        self.account = None
        """the domain ID with which the VLAN IP range is associated.  If used with the account parameter, returns all VLAN IP ranges for that account in the specified domain."""
        self.domainid = None
        """true if VLAN is of Virtual type, false if Direct"""
        self.forvirtualnetwork = None
        """the ID of the VLAN IP range"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """network id of the VLAN IP range"""
        self.networkid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """physical network id of the VLAN IP range"""
        self.physicalnetworkid = None
        """the Pod ID of the VLAN IP range"""
        self.podid = None
        """project who will own the VLAN"""
        self.projectid = None
        """the ID or VID of the VLAN. Default is an "untagged" VLAN."""
        self.vlan = None
        """the Zone ID of the VLAN IP range"""
        self.zoneid = None
        self.required = []

class listVlanIpRangesResponse (baseResponse):
    def __init__(self):
        """the ID of the VLAN IP range"""
        self.id = None
        """the account of the VLAN IP range"""
        self.account = None
        """the description of the VLAN IP range"""
        self.description = None
        """the domain name of the VLAN IP range"""
        self.domain = None
        """the domain ID of the VLAN IP range"""
        self.domainid = None
        """the end ip of the VLAN IP range"""
        self.endip = None
        """the virtual network for the VLAN IP range"""
        self.forvirtualnetwork = None
        """the gateway of the VLAN IP range"""
        self.gateway = None
        """the netmask of the VLAN IP range"""
        self.netmask = None
        """the network id of vlan range"""
        self.networkid = None
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        """the Pod ID for the VLAN IP range"""
        self.podid = None
        """the Pod name for the VLAN IP range"""
        self.podname = None
        """the project name of the vlan range"""
        self.project = None
        """the project id of the vlan range"""
        self.projectid = None
        """the start ip of the VLAN IP range"""
        self.startip = None
        """the ID or VID of the VLAN."""
        self.vlan = None
        """the Zone ID of the VLAN IP range"""
        self.zoneid = None
