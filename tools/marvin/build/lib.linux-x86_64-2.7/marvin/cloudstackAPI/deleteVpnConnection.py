
"""Delete site to site vpn connection"""
from baseCmd import *
from baseResponse import *
class deleteVpnConnectionCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of vpn connection"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVpnConnectionResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

