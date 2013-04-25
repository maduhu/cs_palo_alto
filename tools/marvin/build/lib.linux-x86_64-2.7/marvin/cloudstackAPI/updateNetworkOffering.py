
"""Updates a network offering."""
from baseCmd import *
from baseResponse import *
class updateNetworkOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the availability of network offering. Default value is Required for Guest Virtual network offering; Optional for Guest Direct network offering"""
        self.availability = None
        """the display text of the network offering"""
        self.displaytext = None
        """the id of the network offering"""
        self.id = None
        """the name of the network offering"""
        self.name = None
        """sort key of the network offering, integer"""
        self.sortkey = None
        """update state for the network offering"""
        self.state = None
        self.required = []

class updateNetworkOfferingResponse (baseResponse):
    def __init__(self):
        """the id of the network offering"""
        self.id = None
        """availability of the network offering"""
        self.availability = None
        """true if network offering is ip conserve mode enabled"""
        self.conservemode = None
        """the date this network offering was created"""
        self.created = None
        """an alternate display text of the network offering."""
        self.displaytext = None
        """true if network offering can be used by VPC networks only"""
        self.forvpc = None
        """guest type of the network offering, can be Shared or Isolated"""
        self.guestiptype = None
        """true if network offering is default, false otherwise"""
        self.isdefault = None
        """the name of the network offering"""
        self.name = None
        """data transfer rate in megabits per second allowed."""
        self.networkrate = None
        """the ID of the service offering used by virtual router provider"""
        self.serviceofferingid = None
        """true if network offering supports specifying ip ranges, false otherwise"""
        self.specifyipranges = None
        """true if network offering supports vlans, false otherwise"""
        self.specifyvlan = None
        """state of the network offering. Can be Disabled/Enabled/Inactive"""
        self.state = None
        """the tags for the network offering"""
        self.tags = None
        """the traffic type for the network offering, supported types are Public, Management, Control, Guest, Vlan or Storage."""
        self.traffictype = None
        """the list of supported services"""
        self.service = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the service provider name"""
        self.provider = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

