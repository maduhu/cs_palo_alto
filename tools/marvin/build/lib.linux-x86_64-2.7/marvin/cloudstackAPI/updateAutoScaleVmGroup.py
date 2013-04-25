
"""Updates an existing autoscale vm group."""
from baseCmd import *
from baseResponse import *
class updateAutoScaleVmGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale group"""
        """Required"""
        self.id = None
        """the frequency at which the conditions have to be evaluated"""
        self.interval = None
        """the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."""
        self.maxmembers = None
        """the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."""
        self.minmembers = None
        """list of scaledown autoscale policies"""
        self.scaledownpolicyids = []
        """list of scaleup autoscale policies"""
        self.scaleuppolicyids = []
        self.required = ["id",]

class updateAutoScaleVmGroupResponse (baseResponse):
    def __init__(self):
        """the autoscale vm group ID"""
        self.id = None
        """the account owning the instance group"""
        self.account = None
        """the domain name of the vm profile"""
        self.domain = None
        """the domain ID of the vm profile"""
        self.domainid = None
        """the frequency at which the conditions have to be evaluated"""
        self.interval = None
        """the load balancer rule ID"""
        self.lbruleid = None
        """the maximum number of members in the vmgroup, The number of instances in the vm group will be equal to or less than this number."""
        self.maxmembers = None
        """the minimum number of members in the vmgroup, the number of instances in the vm group will be equal to or more than this number."""
        self.minmembers = None
        """the project name of the vm profile"""
        self.project = None
        """the project id vm profile"""
        self.projectid = None
        """list of scaledown autoscale policies"""
        self.scaledownpolicies = None
        """list of scaleup autoscale policies"""
        self.scaleuppolicies = None
        """the current state of the AutoScale Vm Group"""
        self.state = None
        """the autoscale profile that contains information about the vms in the vm group."""
        self.vmprofileid = None

