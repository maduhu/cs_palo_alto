
"""Deletes a snapshot of a disk volume."""
from baseCmd import *
from baseResponse import *
class deleteSnapshotCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """The ID of the snapshot"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteSnapshotResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

