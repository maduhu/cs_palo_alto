
"""Updates a disk offering."""
from baseCmd import *
from baseResponse import *
class deleteDiskOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """ID of the disk offering"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteDiskOfferingResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

