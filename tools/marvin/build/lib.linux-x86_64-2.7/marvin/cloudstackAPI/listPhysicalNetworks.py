
"""Lists physical networks"""
from baseCmd import *
from baseResponse import *
class listPhysicalNetworksCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list physical network by id"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """search by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the Zone ID for the physical network"""
        self.zoneid = None
        self.required = []

class listPhysicalNetworksResponse (baseResponse):
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

