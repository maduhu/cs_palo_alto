
"""Deletes a Zone."""
from baseCmd import *
from baseResponse import *
class deleteZoneCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the ID of the Zone"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteZoneResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

