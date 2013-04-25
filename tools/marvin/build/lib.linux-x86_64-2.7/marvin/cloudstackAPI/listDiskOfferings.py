
"""Lists all available disk offerings."""
from baseCmd import *
from baseResponse import *
class listDiskOfferingsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the domain of the disk offering."""
        self.domainid = None
        """ID of the disk offering"""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """name of the disk offering"""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = []

class listDiskOfferingsResponse (baseResponse):
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

