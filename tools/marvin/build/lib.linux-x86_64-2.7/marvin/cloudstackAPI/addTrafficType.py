
"""Adds traffic type to a physical network"""
from baseCmd import *
from baseResponse import *
class addTrafficTypeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the Physical Network ID"""
        """Required"""
        self.physicalnetworkid = None
        """the trafficType to be added to the physical network"""
        """Required"""
        self.traffictype = None
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        """The VLAN id to be used for Management traffic by VMware host"""
        self.vlan = None
        """The network name label of the physical device dedicated to this traffic on a VMware host"""
        self.vmwarenetworklabel = None
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.required = ["physicalnetworkid","traffictype",]

class addTrafficTypeResponse (baseResponse):
    def __init__(self):
        """id of the network provider"""
        self.id = None
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        """the trafficType to be added to the physical network"""
        self.traffictype = None
        """The network name label of the physical device dedicated to this traffic on a VMware host"""
        self.vmwarenetworklabel = None
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None

