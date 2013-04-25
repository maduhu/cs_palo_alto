
"""Creates a template of a virtual machine. The virtual machine must be in a STOPPED state. A template created from this command is automatically designated as a private template visible to the account that created it."""
from baseCmd import *
from baseResponse import *
class createTemplateCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the display text of the template. This is usually used for display purposes."""
        """Required"""
        self.displaytext = None
        """the name of the template"""
        """Required"""
        self.name = None
        """the ID of the OS Type that best represents the OS of this template."""
        """Required"""
        self.ostypeid = None
        """32 or 64 bit"""
        self.bits = None
        """Template details in key/value pairs."""
        self.details = []
        """true if this template is a featured template, false otherwise"""
        self.isfeatured = None
        """true if this template is a public template, false otherwise"""
        self.ispublic = None
        """true if the template supports the password reset feature; default is false"""
        self.passwordenabled = None
        """true if the template requres HVM, false otherwise"""
        self.requireshvm = None
        """the ID of the snapshot the template is being created from. Either this parameter, or volumeId has to be passed in"""
        self.snapshotid = None
        """the tag for this template."""
        self.templatetag = None
        """Optional, only for baremetal hypervisor. The directory name where template stored on CIFS server"""
        self.url = None
        """Optional, VM ID. If this presents, it is going to create a baremetal template for VM this ID refers to. This is only for VM whose hypervisor type is BareMetal"""
        self.virtualmachineid = None
        """the ID of the disk volume the template is being created from. Either this parameter, or snapshotId has to be passed in"""
        self.volumeid = None
        self.required = ["displaytext","name","ostypeid",]

class createTemplateResponse (baseResponse):
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

