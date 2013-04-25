
"""Deletes a storage pool."""
from baseCmd import *
from baseResponse import *
class deleteStoragePoolCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Storage pool id"""
        """Required"""
        self.id = None
        """Force destroy storage pool (force expunge volumes in Destroyed state as a part of pool removal)"""
        self.forced = None
        self.required = ["id",]

class deleteStoragePoolResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

