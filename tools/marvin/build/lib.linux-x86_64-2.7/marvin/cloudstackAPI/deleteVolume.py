
"""Deletes a detached disk volume."""
from baseCmd import *
from baseResponse import *
class deleteVolumeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """The ID of the disk volume"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVolumeResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

