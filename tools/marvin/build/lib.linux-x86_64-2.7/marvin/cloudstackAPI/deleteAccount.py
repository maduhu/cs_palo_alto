
"""Deletes a account, and all users associated with this account"""
from baseCmd import *
from baseResponse import *
class deleteAccountCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """Account id"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteAccountResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

