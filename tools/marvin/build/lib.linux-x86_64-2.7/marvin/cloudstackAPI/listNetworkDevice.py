
"""List network devices"""
from baseCmd import *
from baseResponse import *
class listNetworkDeviceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """parameters for network device"""
        self.networkdeviceparameterlist = []
        """Network device type, now supports ExternalDhcp, PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall"""
        self.networkdevicetype = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listNetworkDeviceResponse (baseResponse):
    def __init__(self):
        """the ID of the network device"""
        self.id = None

