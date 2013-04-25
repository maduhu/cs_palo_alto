
"""Deletes a project"""
from baseCmd import *
from baseResponse import *
class deleteProjectCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of the project to be deleted"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteProjectResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

