
"""Creates a service offering."""
from baseCmd import *
from baseResponse import *
class createServiceOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the CPU number of the service offering"""
        """Required"""
        self.cpunumber = None
        """the CPU speed of the service offering in MHz."""
        """Required"""
        self.cpuspeed = None
        """the display text of the service offering"""
        """Required"""
        self.displaytext = None
        """the total memory of the service offering in MB"""
        """Required"""
        self.memory = None
        """the name of the service offering"""
        """Required"""
        self.name = None
        """the ID of the containing domain, null for public offerings"""
        self.domainid = None
        """the host tag for this service offering."""
        self.hosttags = None
        """is this a system vm offering"""
        self.issystem = None
        """restrict the CPU usage to committed service offering"""
        self.limitcpuuse = None
        """data transfer rate in megabits per second allowed. Supported only for non-System offering and system offerings having "domainrouter" systemvmtype"""
        self.networkrate = None
        """the HA for the service offering"""
        self.offerha = None
        """the storage type of the service offering. Values are local and shared."""
        self.storagetype = None
        """the system VM type. Possible types are "domainrouter", "consoleproxy" and "secondarystoragevm"."""
        self.systemvmtype = None
        """the tags for this service offering."""
        self.tags = None
        self.required = ["cpunumber","cpuspeed","displaytext","memory","name",]

class createServiceOfferingResponse (baseResponse):
    def __init__(self):
        """the id of the service offering"""
        self.id = None
        """the number of CPU"""
        self.cpunumber = None
        """the clock rate CPU speed in Mhz"""
        self.cpuspeed = None
        """the date this service offering was created"""
        self.created = None
        """is this a  default system vm offering"""
        self.defaultuse = None
        """an alternate display text of the service offering."""
        self.displaytext = None
        """Domain name for the offering"""
        self.domain = None
        """the domain id of the service offering"""
        self.domainid = None
        """the host tag for the service offering"""
        self.hosttags = None
        """is this a system vm offering"""
        self.issystem = None
        """restrict the CPU usage to committed service offering"""
        self.limitcpuuse = None
        """the memory in MB"""
        self.memory = None
        """the name of the service offering"""
        self.name = None
        """data transfer rate in megabits per second allowed."""
        self.networkrate = None
        """the ha support in the service offering"""
        self.offerha = None
        """the storage type for this service offering"""
        self.storagetype = None
        """is this a the systemvm type for system vm offering"""
        self.systemvmtype = None
        """the tags for the service offering"""
        self.tags = None

