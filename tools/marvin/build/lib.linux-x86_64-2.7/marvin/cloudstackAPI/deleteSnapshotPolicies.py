
"""Deletes snapshot policies for the account."""
from baseCmd import *
from baseResponse import *
class deleteSnapshotPoliciesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the Id of the snapshot policy"""
        self.id = None
        """list of snapshots policy IDs separated by comma"""
        self.ids = []
        self.required = []

class deleteSnapshotPoliciesResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

