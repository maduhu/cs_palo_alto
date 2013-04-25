
"""Updates a physical network"""
from baseCmd import *
from baseResponse import *
class updatePhysicalNetworkCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """physical network id"""
        """Required"""
        self.id = None
        """the speed for the physical network[1G/10G]"""
        self.networkspeed = None
        """Enabled/Disabled"""
        self.state = None
        """Tag the physical network"""
        self.tags = []
        """the VLAN for the physical network"""
        self.vlan = None
        self.required = ["id",]

class updatePhysicalNetworkResponse (baseResponse):
    def __init__(self):
        """the uuid of the physical network"""
        self.id = None
        """Broadcast domain range of the physical network"""
        self.broadcastdomainrange = None
        """the domain id of the physical network owner"""
        self.domainid = None
        """isolation methods"""
        self.isolationmethods = None
        """name of the physical network"""
        self.name = None
        """the speed of the physical network"""
        self.networkspeed = None
        """state of the physical network"""
        self.state = None
        """comma separated tag"""
        self.tags = None
        """the vlan of the physical network"""
        self.vlan = None
        """zone id of the physical network"""
        self.zoneid = None

