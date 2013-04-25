
"""Disables static rule for given ip address"""
from baseCmd import *
from baseResponse import *
class disableStaticNatCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the public IP address id for which static nat feature is being disableed"""
        """Required"""
        self.ipaddressid = None
        self.required = ["ipaddressid",]

class disableStaticNatResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

