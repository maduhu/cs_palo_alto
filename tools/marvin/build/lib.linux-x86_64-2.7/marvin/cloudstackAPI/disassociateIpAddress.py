
"""Disassociates an ip address from the account."""
from baseCmd import *
from baseResponse import *
class disassociateIpAddressCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the id of the public ip address to disassociate"""
        """Required"""
        self.id = None
        self.required = ["id",]

class disassociateIpAddressResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

