
"""Deletes a service offering."""
from baseCmd import *
from baseResponse import *
class deleteServiceOfferingCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the service offering"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteServiceOfferingResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

