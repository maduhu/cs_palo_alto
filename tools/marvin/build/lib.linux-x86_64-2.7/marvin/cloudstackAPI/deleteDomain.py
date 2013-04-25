
"""Deletes a specified domain"""
from baseCmd import *
from baseResponse import *
class deleteDomainCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """ID of domain to delete"""
        """Required"""
        self.id = None
        """true if all domain resources (child domains, accounts) have to be cleaned up, false otherwise"""
        self.cleanup = None
        self.required = ["id",]

class deleteDomainResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

