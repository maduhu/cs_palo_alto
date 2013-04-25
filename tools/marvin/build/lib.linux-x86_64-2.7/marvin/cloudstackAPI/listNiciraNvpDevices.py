
"""Lists Nicira NVP devices"""
from baseCmd import *
from baseResponse import *
class listNiciraNvpDevicesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """nicira nvp device ID"""
        self.nvpdeviceid = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """the Physical Network ID"""
        self.physicalnetworkid = None
        self.required = []

class listNiciraNvpDevicesResponse (baseResponse):
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

