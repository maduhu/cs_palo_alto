
"""Lists all network services provided by CloudStack or for the given Provider."""
from baseCmd import *
from baseResponse import *
class listSupportedNetworkServicesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """network service provider name"""
        self.provider = None
        """network service name to list providers and capabilities of"""
        self.service = None
        self.required = []

class listSupportedNetworkServicesResponse (baseResponse):
    def __init__(self):
        """the service name"""
        self.name = None
        """the service provider name"""
        self.provider = None
        """the list of capabilities"""
        self.capability = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

