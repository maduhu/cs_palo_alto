
"""Delete site to site vpn customer gateway"""
from baseCmd import *
from baseResponse import *
class deleteVpnCustomerGatewayCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """id of customer gateway"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteVpnCustomerGatewayResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

