
"""Lists all hypervisor capabilities."""
from baseCmd import *
from baseResponse import *
class listHypervisorCapabilitiesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the hypervisor for which to restrict the search"""
        self.hypervisor = None
        """ID of the hypervisor capability"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listHypervisorCapabilitiesResponse (baseResponse):
    def __init__(self):
        """the ID of the hypervisor capabilities row"""
        self.id = None
        """the hypervisor type"""
        self.hypervisor = None
        """the hypervisor version"""
        self.hypervisorversion = None
        """the maximum number of guest vms recommended for this hypervisor"""
        self.maxguestslimit = None
        """true if security group is supported"""
        self.securitygroupenabled = None

