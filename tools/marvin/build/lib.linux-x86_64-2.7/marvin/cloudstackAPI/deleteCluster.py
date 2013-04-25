
"""Deletes a cluster."""
from baseCmd import *
from baseResponse import *
class deleteClusterCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the cluster ID"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteClusterResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

