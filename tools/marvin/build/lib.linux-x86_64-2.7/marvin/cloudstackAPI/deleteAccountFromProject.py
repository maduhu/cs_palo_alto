
"""Deletes account from the project"""
from baseCmd import *
from baseResponse import *
class deleteAccountFromProjectCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """name of the account to be removed from the project"""
        """Required"""
        self.account = None
        """id of the project to remove the account from"""
        """Required"""
        self.projectid = None
        self.required = ["account","projectid",]

class deleteAccountFromProjectResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

