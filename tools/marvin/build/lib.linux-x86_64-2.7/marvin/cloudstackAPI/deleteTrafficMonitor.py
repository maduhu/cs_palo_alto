
"""Deletes an traffic monitor host."""
from baseCmd import *
from baseResponse import *
class deleteTrafficMonitorCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """Id of the Traffic Monitor Host."""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteTrafficMonitorResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

