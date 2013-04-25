
"""Delete site to site vpn gateway"""
from baseCmd import *
from baseResponse import *
class deleteVpnGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of customer gateway"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVpnGatewayResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

