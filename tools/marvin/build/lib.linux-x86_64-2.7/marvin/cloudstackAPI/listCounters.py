
"""List the counters"""
from baseCmd import *
from baseResponse import *
class listCountersCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """ID of the Counter."""
        self.id = None
        """List by keyword"""
        self.keyword = None
        """Name of the counter."""
        self.name = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """Source of the counter."""
        self.source = None
        self.required = []

class listCountersResponse (baseResponse):
    def __init__(self):
        """the id of the Counter"""
        self.id = None
        """Name of the counter."""
        self.name = None
        """Source of the counter."""
        self.source = None
        """Value in case of snmp or other specific counters."""
        self.value = None
        """zone id of counter"""
        self.zoneid = None

