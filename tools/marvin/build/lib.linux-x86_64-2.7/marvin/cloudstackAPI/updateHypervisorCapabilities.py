
"""Updates a hypervisor capabilities."""
from baseCmd import *
from baseResponse import *
class updateHypervisorCapabilitiesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """ID of the hypervisor capability"""
        self.id = None
        """the max number of Guest VMs per host for this hypervisor."""
        self.maxguestslimit = None
        """set true to enable security group for this hypervisor."""
        self.securitygroupenabled = None
        self.required = []

class updateHypervisorCapabilitiesResponse (baseResponse):
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

