
"""Deletes VPC offering"""
from baseCmd import *
from baseResponse import *
class deleteVPCOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the VPC offering"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVPCOfferingResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

