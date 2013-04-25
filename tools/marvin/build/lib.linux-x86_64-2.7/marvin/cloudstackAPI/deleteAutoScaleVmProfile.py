
"""Deletes a autoscale vm profile."""
from baseCmd import *
from baseResponse import *
class deleteAutoScaleVmProfileCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the autoscale profile"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteAutoScaleVmProfileResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

