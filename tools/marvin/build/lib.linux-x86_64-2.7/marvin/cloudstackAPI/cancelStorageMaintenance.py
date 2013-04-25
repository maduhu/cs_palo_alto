
"""Cancels maintenance for primary storage"""
from baseCmd import *
from baseResponse import *
class cancelStorageMaintenanceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the primary storage ID"""
        """Required"""
        self.id = None
        self.required = ["id",]

class cancelStorageMaintenanceResponse (baseResponse):
    def __init__(self):
        """the ID of the storage pool"""
        self.id = None
        """the ID of the cluster for the storage pool"""
        self.clusterid = None
        """the name of the cluster for the storage pool"""
        self.clustername = None
        """the date and time the storage pool was created"""
        self.created = None
        """the host's currently allocated disk size"""
        self.disksizeallocated = None
        """the total disk size of the storage pool"""
        self.disksizetotal = None
        """the host's currently used disk size"""
        self.disksizeused = None
        """the IP address of the storage pool"""
        self.ipaddress = None
        """the name of the storage pool"""
        self.name = None
        """the storage pool path"""
        self.path = None
        """the Pod ID of the storage pool"""
        self.podid = None
        """the Pod name of the storage pool"""
        self.podname = None
        """the state of the storage pool"""
        self.state = None
        """the tags for the storage pool"""
        self.tags = None
        """the storage pool type"""
        self.type = None
        """the Zone ID of the storage pool"""
        self.zoneid = None
        """the Zone name of the storage pool"""
        self.zonename = None
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None

