
"""Updates a network serviceProvider of a physical network"""
from baseCmd import *
from baseResponse import *
class updateNetworkServiceProviderCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """network service provider id"""
        """Required"""
        self.id = None
        """the list of services to be enabled for this physical network service provider"""
        self.servicelist = []
        """Enabled/Disabled/Shutdown the physical network service provider"""
        self.state = None
        self.required = ["id",]

class updateNetworkServiceProviderResponse (baseResponse):
    def __init__(self):
        """uuid of the network provider"""
        self.id = None
        """true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """the destination physical network"""
        self.destinationphysicalnetworkid = None
        """the provider name"""
        self.name = None
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        """services for this provider"""
        self.servicelist = None
        """state of the network provider"""
        self.state = None

