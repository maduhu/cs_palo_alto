
"""Lists clusters."""
from baseCmd import *
from baseResponse import *
class listClustersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """lists clusters by allocation state"""
        self.allocationstate = None
        """lists clusters by cluster type"""
        self.clustertype = None
        """lists clusters by hypervisor type"""
        self.hypervisor = None
        """lists clusters by the cluster ID"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """whether this cluster is managed by cloudstack"""
        self.managedstate = None
        """lists clusters by the cluster name"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """lists clusters by Pod ID"""
        self.podid = None
        """flag to display the capacity of the clusters"""
        self.showcapacities = None
        """lists clusters by Zone ID"""
        self.zoneid = None
        self.required = []

class listClustersResponse (baseResponse):
    def __init__(self):
        """the cluster ID"""
        self.id = None
        """the allocation state of the cluster"""
        self.allocationstate = None
        """the type of the cluster"""
        self.clustertype = None
        """the hypervisor type of the cluster"""
        self.hypervisortype = None
        """whether this cluster is managed by cloudstack"""
        self.managedstate = None
        """the cluster name"""
        self.name = None
        """the Pod ID of the cluster"""
        self.podid = None
        """the Pod name of the cluster"""
        self.podname = None
        """the Zone ID of the cluster"""
        self.zoneid = None
        """the Zone name of the cluster"""
        self.zonename = None
        """the capacity of the Cluster"""
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

