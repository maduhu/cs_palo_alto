
"""Creates a Zone."""
from baseCmd import *
from baseResponse import *
class createZoneCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the first DNS for the Zone"""
        """Required"""
        self.dns1 = None
        """the first internal DNS for the Zone"""
        """Required"""
        self.internaldns1 = None
        """the name of the Zone"""
        """Required"""
        self.name = None
        """network type of the zone, can be Basic or Advanced"""
        """Required"""
        self.networktype = None
        """Allocation state of this Zone for allocation of new resources"""
        self.allocationstate = None
        """the second DNS for the Zone"""
        self.dns2 = None
        """Network domain name for the networks in the zone"""
        self.domain = None
        """the ID of the containing domain, null for public zones"""
        self.domainid = None
        """the guest CIDR address for the Zone"""
        self.guestcidraddress = None
        """the second internal DNS for the Zone"""
        self.internaldns2 = None
        """true if local storage offering enabled, false otherwise"""
        self.localstorageenabled = None
        """true if network is security group enabled, false otherwise"""
        self.securitygroupenabled = None
        self.required = ["dns1","internaldns1","name","networktype",]

class createZoneResponse (baseResponse):
    def __init__(self):
        """Zone id"""
        self.id = None
        """the allocation state of the cluster"""
        self.allocationstate = None
        """Zone description"""
        self.description = None
        """the dhcp Provider for the Zone"""
        self.dhcpprovider = None
        """the display text of the zone"""
        self.displaytext = None
        """the first DNS for the Zone"""
        self.dns1 = None
        """the second DNS for the Zone"""
        self.dns2 = None
        """Network domain name for the networks in the zone"""
        self.domain = None
        """the UUID of the containing domain, null for public zones"""
        self.domainid = None
        """the name of the containing domain, null for public zones"""
        self.domainname = None
        """the guest CIDR address for the Zone"""
        self.guestcidraddress = None
        """the first internal DNS for the Zone"""
        self.internaldns1 = None
        """the second internal DNS for the Zone"""
        self.internaldns2 = None
        """true if local storage offering enabled, false otherwise"""
        self.localstorageenabled = None
        """Zone name"""
        self.name = None
        """the network type of the zone; can be Basic or Advanced"""
        self.networktype = None
        """true if security groups support is enabled, false otherwise"""
        self.securitygroupsenabled = None
        """the vlan range of the zone"""
        self.vlan = None
        """Zone Token"""
        self.zonetoken = None
        """the capacity of the Zone"""
        self.capacity = []

class capacity:
    def __init__(self):
        """"the total capacity available"""
        self.capacitytotal = None
        """"the capacity currently in use"""
        self.capacityused = None
        """"the Cluster ID"""
        self.clusterid = None
        """"the Cluster name"""
        self.clustername = None
        """"the percentage of capacity currently in use"""
        self.percentused = None
        """"the Pod ID"""
        self.podid = None
        """"the Pod name"""
        self.podname = None
        """"the capacity type"""
        self.type = None
        """"the Zone ID"""
        self.zoneid = None
        """"the Zone name"""
        self.zonename = None

