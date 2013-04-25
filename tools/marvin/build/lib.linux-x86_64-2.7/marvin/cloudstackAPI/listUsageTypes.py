
"""List Usage Types"""
from baseCmd import *
from baseResponse import *
class listUsageTypesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class listUsageTypesResponse (baseResponse):
    def __init__(self):
        """description of usage type"""
        self.description = None
        """usage type"""
        self.usagetypeid = None

