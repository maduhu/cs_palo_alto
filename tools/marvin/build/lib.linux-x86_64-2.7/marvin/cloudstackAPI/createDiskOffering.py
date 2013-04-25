
"""Creates a disk offering."""
from baseCmd import *
from baseResponse import *
class createDiskOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """alternate display text of the disk offering"""
        """Required"""
        self.displaytext = None
        """name of the disk offering"""
        """Required"""
        self.name = None
        """whether disk offering is custom or not"""
        self.customized = None
        """size of the disk offering in GB"""
        self.disksize = None
        """the ID of the containing domain, null for public offerings"""
        self.domainid = None
        """the storage type of the disk offering. Values are local and shared."""
        self.storagetype = None
        """tags for the disk offering"""
        self.tags = None
        self.required = ["displaytext","name",]

class createDiskOfferingResponse (baseResponse):
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

