
"""Deletes a Pod."""
from baseCmd import *
from baseResponse import *
class deletePodCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the Pod"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deletePodResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

