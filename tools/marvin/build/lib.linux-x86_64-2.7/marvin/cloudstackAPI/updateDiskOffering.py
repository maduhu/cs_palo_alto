
"""Updates a disk offering."""
from baseCmd import *
from baseResponse import *
class updateDiskOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """ID of the disk offering"""
        """Required"""
        self.id = None
        """updates alternate display text of the disk offering with this value"""
        self.displaytext = None
        """updates name of the disk offering with this value"""
        self.name = None
        """sort key of the disk offering, integer"""
        self.sortkey = None
        self.required = ["id",]

class updateDiskOfferingResponse (baseResponse):
    def __init__(self):
        """unique ID of the disk offering"""
        self.id = None
        """the date this disk offering was created"""
        self.created = None
        """the size of the disk offering in GB"""
        self.disksize = None
        """an alternate display text of the disk offering."""
        self.displaytext = None
        """the domain name this disk offering belongs to. Ignore this information as it is not currently applicable."""
        self.domain = None
        """the domain ID this disk offering belongs to. Ignore this information as it is not currently applicable."""
        self.domainid = None
        """true if disk offering uses custom size, false otherwise"""
        self.iscustomized = None
        """the name of the disk offering"""
        self.name = None
        """the storage type for this disk offering"""
        self.storagetype = None
        """the tags for the disk offering"""
        self.tags = None

