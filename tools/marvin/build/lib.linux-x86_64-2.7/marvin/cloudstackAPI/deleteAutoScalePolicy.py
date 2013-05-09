
"""Deletes a autoscale policy."""
from baseCmd import *
from baseResponse import *
class deleteAutoScalePolicyCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale policy"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteAutoScalePolicyResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None
