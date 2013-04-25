
"""Adds a new cluster"""
from baseCmd import *
from baseResponse import *
class addClusterCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the cluster name"""
        """Required"""
        self.clustername = None
        """type of the cluster: CloudManaged, ExternalManaged"""
        """Required"""
        self.clustertype = None
        """hypervisor type of the cluster: XenServer,KVM,VMware,Hyperv,BareMetal,Simulator"""
        """Required"""
        self.hypervisor = None
        """the Pod ID for the host"""
        """Required"""
        self.podid = None
        """the Zone ID for the cluster"""
        """Required"""
        self.zoneid = None
        """Allocation state of this cluster for allocation of new resources"""
        self.allocationstate = None
        """the password for the host"""
        self.password = None
        """the URL"""
        self.url = None
        """the username for the cluster"""
        self.username = None
        """the ipaddress of the VSM associated with this cluster"""
        self.vsmipaddress = None
        """the password for the VSM associated with this cluster"""
        self.vsmpassword = None
        """the username for the VSM associated with this cluster"""
        self.vsmusername = None
        self.required = ["clustername","clustertype","hypervisor","podid","zoneid",]

class addClusterResponse (baseResponse):
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

