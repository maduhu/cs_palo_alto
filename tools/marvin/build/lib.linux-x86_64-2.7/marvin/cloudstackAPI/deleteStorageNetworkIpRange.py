
"""Deletes a storage network IP Range."""
from baseCmd import *
from baseResponse import *
class deleteStorageNetworkIpRangeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the uuid of the storage network ip range"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteStorageNetworkIpRangeResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

