
"""Update a Storage network IP range, only allowed when no IPs in this range have been allocated."""
from baseCmd import *
from baseResponse import *
class updateStorageNetworkIpRangeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """UUID of storage network ip range"""
        """Required"""
        self.id = None
        """the ending IP address"""
        self.endip = None
        """the netmask for storage network"""
        self.netmask = None
        """the beginning IP address"""
        self.startip = None
        """Optional. the vlan the ip range sits on"""
        self.vlan = None
        self.required = ["id",]

class updateStorageNetworkIpRangeResponse (baseResponse):
    def __init__(self):
        """the uuid of storage network IP range."""
        self.id = None
        """the end ip of the storage network IP range"""
        self.endip = None
        """the gateway of the storage network IP range"""
        self.gateway = None
        """the netmask of the storage network IP range"""
        self.netmask = None
        """the network uuid of storage network IP range"""
        self.networkid = None
        """the Pod uuid for the storage network IP range"""
        self.podid = None
        """the start ip of the storage network IP range"""
        self.startip = None
        """the ID or VID of the VLAN."""
        self.vlan = None
        """the Zone uuid of the storage network IP range"""
        self.zoneid = None

