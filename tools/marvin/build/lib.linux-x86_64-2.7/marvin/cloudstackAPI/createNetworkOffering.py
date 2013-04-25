
"""Creates a network offering."""
from baseCmd import *
from baseResponse import *
class createNetworkOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the display text of the network offering"""
        """Required"""
        self.displaytext = None
        """guest type of the network offering: Shared or Isolated"""
        """Required"""
        self.guestiptype = None
        """the name of the network offering"""
        """Required"""
        self.name = None
        """services supported by the network offering"""
        """Required"""
        self.supportedservices = []
        """the traffic type for the network offering. Supported type in current release is GUEST only"""
        """Required"""
        self.traffictype = None
        """the availability of network offering. Default value is Optional"""
        self.availability = None
        """true if the network offering is IP conserve mode enabled"""
        self.conservemode = None
        """data transfer rate in megabits per second allowed"""
        self.networkrate = None
        """desired service capabilities as part of network offering"""
        self.servicecapabilitylist = []
        """the service offering ID used by virtual router provider"""
        self.serviceofferingid = None
        """provider to service mapping. If not specified, the provider for the service will be mapped to the default provider on the physical network"""
        self.serviceproviderlist = []
        """true if network offering supports specifying ip ranges; defaulted to false if not specified"""
        self.specifyipranges = None
        """true if network offering supports vlans"""
        self.specifyvlan = None
        """the tags for the network offering."""
        self.tags = None
        self.required = ["displaytext","guestiptype","name","supportedservices","traffictype",]

class createNetworkOfferingResponse (baseResponse):
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

