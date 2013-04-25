
"""Destroys a l2tp/ipsec remote access vpn"""
from baseCmd import *
from baseResponse import *
class deleteRemoteAccessVpnCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """public ip address id of the vpn server"""
        """Required"""
        self.publicipid = None
        self.required = ["publicipid",]

class deleteRemoteAccessVpnResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

