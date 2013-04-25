
"""List traffic monitor Hosts."""
from baseCmd import *
from baseResponse import *
class listTrafficMonitorsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """zone Id"""
        """Required"""
        self.zoneid = None
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        self.required = ["zoneid",]

class listTrafficMonitorsResponse (baseResponse):
    def __init__(self):
        """the ID of the external firewall"""
        self.id = None
        """the management IP address of the external firewall"""
        self.ipaddress = None
        """the number of times to retry requests to the external firewall"""
        self.numretries = None
        """the timeout (in seconds) for requests to the external firewall"""
        self.timeout = None
        """the zone ID of the external firewall"""
        self.zoneid = None

