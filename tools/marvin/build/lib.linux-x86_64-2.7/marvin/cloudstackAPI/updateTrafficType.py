
"""Updates traffic type of a physical network"""
from baseCmd import *
from baseResponse import *
class updateTrafficTypeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """traffic type id"""
        """Required"""
        self.id = None
        """The network name label of the physical device dedicated to this traffic on a KVM host"""
        self.kvmnetworklabel = None
        """The network name label of the physical device dedicated to this traffic on a VMware host"""
        self.vmwarenetworklabel = None
        """The network name label of the physical device dedicated to this traffic on a XenServer host"""
        self.xennetworklabel = None
        self.required = ["id",]

class updateTrafficTypeResponse (baseResponse):
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

