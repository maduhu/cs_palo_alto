
"""Adds a Nicira NVP device"""
from baseCmd import *
from baseResponse import *
class addNiciraNvpDeviceCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """Hostname of ip address of the Nicira NVP Controller."""
        """Required"""
        self.hostname = None
        """Credentials to access the Nicira Controller API"""
        """Required"""
        self.password = None
        """the Physical Network ID"""
        """Required"""
        self.physicalnetworkid = None
        """The Transportzone UUID configured on the Nicira Controller"""
        """Required"""
        self.transportzoneuuid = None
        """Credentials to access the Nicira Controller API"""
        """Required"""
        self.username = None
        """The L3 Gateway Service UUID configured on the Nicira Controller"""
        self.l3gatewayserviceuuid = None
        self.required = ["hostname","password","physicalnetworkid","transportzoneuuid","username",]

class addNiciraNvpDeviceResponse (baseResponse):
    def __init__(self):
        """the controller Ip address"""
        self.hostname = None
        """this L3 gateway service Uuid"""
        self.l3gatewayserviceuuid = None
        """device name"""
        self.niciradevicename = None
        """device id of the Nicire Nvp"""
        self.nvpdeviceid = None
        """the physical network to which this Nirica Nvp belongs to"""
        self.physicalnetworkid = None
        """name of the provider"""
        self.provider = None
        """the transport zone Uuid"""
        self.transportzoneuuid = None

