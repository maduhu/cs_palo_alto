
"""Deletes a host."""
from baseCmd import *
from baseResponse import *
class deleteHostCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the host ID"""
        """Required"""
        self.id = None
        """Force delete the host. All HA enabled vms running on the host will be put to HA; HA disabled ones will be stopped"""
        self.forced = None
        """Force destroy local storage on this host. All VMs created on this local storage will be destroyed"""
        self.forcedestroylocalstorage = None
        self.required = ["id",]

class deleteHostResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

