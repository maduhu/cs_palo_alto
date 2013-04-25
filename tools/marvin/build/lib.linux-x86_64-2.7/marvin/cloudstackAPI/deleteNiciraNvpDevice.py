
"""delete a nicira nvp device"""
from baseCmd import *
from baseResponse import *
class deleteNiciraNvpDeviceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """Nicira device ID"""
        """Required"""
        self.nvpdeviceid = None
        self.required = ["nvpdeviceid",]

class deleteNiciraNvpDeviceResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

