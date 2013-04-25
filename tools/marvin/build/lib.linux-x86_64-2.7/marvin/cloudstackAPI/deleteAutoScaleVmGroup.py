
"""Deletes a autoscale vm group."""
from baseCmd import *
from baseResponse import *
class deleteAutoScaleVmGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale group"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteAutoScaleVmGroupResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

