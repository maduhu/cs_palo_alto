
"""Enables static nat for given ip address"""
from baseCmd import *
from baseResponse import *
class enableStaticNatCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the public IP address id for which static nat feature is being enabled"""
        """Required"""
        self.ipaddressid = None
        """the ID of the virtual machine for enabling static nat feature"""
        """Required"""
        self.virtualmachineid = None
        """The network of the vm the static nat will be enabled for. Required when public Ip address is not associated with any Guest network yet (VPC case)"""
        self.networkid = None
        self.required = ["ipaddressid","virtualmachineid",]

class enableStaticNatResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

