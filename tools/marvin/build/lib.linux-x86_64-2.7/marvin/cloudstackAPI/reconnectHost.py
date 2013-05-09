
"""Reconnects a host."""
from baseCmd import *
from baseResponse import *
class reconnectHostCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the host ID"""
        """Required"""
        self.id = None
        self.required = ["id",]

class reconnectHostResponse (baseResponse):
    def __init__(self):
        """the ID of the host"""
        self.id = None
        """the cpu average load on the host"""
        self.averageload = None
        """capabilities of the host"""
        self.capabilities = None
        """the cluster ID of the host"""
        self.clusterid = None
        """the cluster name of the host"""
        self.clustername = None
        """the cluster type of the cluster that host belongs to"""
        self.clustertype = None
        """the amount of the host's CPU currently allocated"""
        self.cpuallocated = None
        """the CPU number of the host"""
        self.cpunumber = None
        """the CPU speed of the host"""
        self.cpuspeed = None
        """the amount of the host's CPU currently used"""
        self.cpuused = None
        """the amount of the host's CPU after applying the cpu.overprovisioning.factor"""
        self.cpuwithoverprovisioning = None
        """the date and time the host was created"""
        self.created = None
        """true if the host is disconnected. False otherwise."""
        self.disconnected = None
        """the host's currently allocated disk size"""
        self.disksizeallocated = None
        """the total disk size of the host"""
        self.disksizetotal = None
        """events available for the host"""
        self.events = None
        """true if the host is Ha host (dedicated to vms started by HA process; false otherwise"""
        self.hahost = None
        """true if this host has enough CPU and RAM capacity to migrate a VM to it, false otherwise"""
        self.hasenoughcapacity = None
        """comma-separated list of tags for the host"""
        self.hosttags = None
        """the host hypervisor"""
        self.hypervisor = None
        """the hypervisor version"""
        self.hypervisorversion = None
        """the IP address of the host"""
        self.ipaddress = None
        """true if local storage is active, false otherwise"""
        self.islocalstorageactive = None
        """the date and time the host was last pinged"""
        self.lastpinged = None
        """the management server ID of the host"""
        self.managementserverid = None
        """the amount of the host's memory currently allocated"""
        self.memoryallocated = None
        """the memory total of the host"""
        self.memorytotal = None
        """the amount of the host's memory currently used"""
        self.memoryused = None
        """the name of the host"""
        self.name = None
        """the incoming network traffic on the host"""
        self.networkkbsread = None
        """the outgoing network traffic on the host"""
        self.networkkbswrite = None
        """the OS category ID of the host"""
        self.oscategoryid = None
        """the OS category name of the host"""
        self.oscategoryname = None
        """the Pod ID of the host"""
        self.podid = None
        """the Pod name of the host"""
        self.podname = None
        """the date and time the host was removed"""
        self.removed = None
        """the resource state of the host"""
        self.resourcestate = None
        """the state of the host"""
        self.state = None
        """true if this host is suitable(has enough capacity and satisfies all conditions like hosttags, max guests vm limit etc) to migrate a VM to it , false otherwise"""
        self.suitableformigration = None
        """the host type"""
        self.type = None
        """the host version"""
        self.version = None
        """the Zone ID of the host"""
        self.zoneid = None
        """the Zone name of the host"""
        self.zonename = None
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
