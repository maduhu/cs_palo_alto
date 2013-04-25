
"""Deletes traffic type of a physical network"""
from baseCmd import *
from baseResponse import *
class deleteTrafficTypeCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """traffic type id"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteTrafficTypeResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

