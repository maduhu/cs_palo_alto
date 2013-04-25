
"""Adds a network device of one of the following types: ExternalDhcp, ExternalFirewall, ExternalLoadBalancer, PxeServer"""
from baseCmd import *
from baseResponse import *
class addNetworkDeviceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """parameters for network device"""
        self.networkdeviceparameterlist = []
        """Network device type, now supports ExternalDhcp, PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall"""
        self.networkdevicetype = None
        self.required = []

class addNetworkDeviceResponse (baseResponse):
    def __init__(self):
        """the ID of the network device"""
        self.id = None

