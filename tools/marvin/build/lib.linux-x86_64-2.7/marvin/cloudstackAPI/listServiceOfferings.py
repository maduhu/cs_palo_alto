
"""Lists all available service offerings."""
from baseCmd import *
from baseResponse import *
class listServiceOfferingsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the domain associated with the service offering"""
        self.domainid = None
        """ID of the service offering"""
        self.id = None
        """is this a system vm offering"""
        self.issystem = None
        """List by keyword"""
        self.keyword = None
        """name of the service offering"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the system VM type. Possible types are "consoleproxy", "secondarystoragevm" or "domainrouter"."""
        self.systemvmtype = None
        """the ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to."""
        self.virtualmachineid = None
        self.required = []

class listServiceOfferingsResponse (baseResponse):
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

