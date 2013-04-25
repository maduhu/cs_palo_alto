
"""Adds acoount to a project"""
from baseCmd import *
from baseResponse import *
class addAccountToProjectCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of the project to add the account to"""
        """Required"""
        self.projectid = None
        """name of the account to be added to the project"""
        self.account = None
        """email to which invitation to the project is going to be sent"""
        self.email = None
        self.required = ["projectid",]

class addAccountToProjectResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

