
"""Lists storage pools."""
from baseCmd import *
from baseResponse import *
class listStoragePoolsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """list storage pools belongig to the specific cluster"""
        self.clusterid = None
        """the ID of the storage pool"""
        self.id = None
        """the IP address for the storage pool"""
        self.ipaddress = None
        """List by keyword"""
        self.keyword = None
        """the name of the storage pool"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the storage pool path"""
        self.path = None
        """the Pod ID for the storage pool"""
        self.podid = None
        """the Zone ID for the storage pool"""
        self.zoneid = None
        self.required = []

class listStoragePoolsResponse (baseResponse):
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

