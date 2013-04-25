
"""Removes a condition"""
from baseCmd import *
from baseResponse import *
class deleteConditionCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the condition."""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteConditionResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

