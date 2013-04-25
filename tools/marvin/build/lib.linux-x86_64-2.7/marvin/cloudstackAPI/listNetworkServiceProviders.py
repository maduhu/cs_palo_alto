
"""Lists network serviceproviders for a given physical network."""
from baseCmd import *
from baseResponse import *
class listNetworkServiceProvidersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """list providers by name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the Physical Network ID"""
        self.physicalnetworkid = None
        """list providers by state"""
        self.state = None
        self.required = []

class listNetworkServiceProvidersResponse (baseResponse):
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

