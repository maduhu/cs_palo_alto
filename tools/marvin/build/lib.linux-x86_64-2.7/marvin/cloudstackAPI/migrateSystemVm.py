
"""Attempts Migration of a system virtual machine to the host specified."""
from baseCmd import *
from baseResponse import *
class migrateSystemVmCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """destination Host ID to migrate VM to"""
        """Required"""
        self.hostid = None
        """the ID of the virtual machine"""
        """Required"""
        self.virtualmachineid = None
        self.required = ["hostid","virtualmachineid",]

class migrateSystemVmResponse (baseResponse):
    def __init__(self):
        """the ID of the system VM"""
        self.id = None
        """the host ID for the system VM"""
        self.hostid = None
        """the name of the system VM"""
        self.name = None
        """the role of the system VM"""
        self.role = None
        """the state of the system VM"""
        self.state = None
        """the system VM type"""
        self.systemvmtype = None

