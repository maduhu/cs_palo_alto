
"""Deletes an ISO file."""
from baseCmd import *
from baseResponse import *
class deleteIsoCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the ISO file"""
        """Required"""
        self.id = None
        """the ID of the zone of the ISO file. If not specified, the ISO will be deleted from all the zones"""
        self.zoneid = None
        self.required = ["id",]

class deleteIsoResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

