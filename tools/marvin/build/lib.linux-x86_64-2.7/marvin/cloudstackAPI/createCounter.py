
"""Adds metric counter"""
from baseCmd import *
from baseResponse import *
class createCounterCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """Name of the counter."""
        """Required"""
        self.name = None
        """Source of the counter."""
        """Required"""
        self.source = None
        """Value of the counter e.g. oid in case of snmp."""
        """Required"""
        self.value = None
        self.required = ["name","source","value",]

class createCounterResponse (baseResponse):
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

