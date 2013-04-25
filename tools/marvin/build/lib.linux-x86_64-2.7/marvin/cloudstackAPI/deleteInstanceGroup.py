
"""Deletes a vm group"""
from baseCmd import *
from baseResponse import *
class deleteInstanceGroupCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the instance group"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteInstanceGroupResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

