
"""Lists traffic types of a given physical network."""
from baseCmd import *
from baseResponse import *
class listTrafficTypesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the Physical Network ID"""
        """Required"""
        self.physicalnetworkid = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = ["physicalnetworkid",]

class listTrafficTypesResponse (baseResponse):
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

