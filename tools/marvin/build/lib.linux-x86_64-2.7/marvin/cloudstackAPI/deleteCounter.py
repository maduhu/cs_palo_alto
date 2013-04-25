
"""Deletes a counter"""
from baseCmd import *
from baseResponse import *
class deleteCounterCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the counter"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteCounterResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

