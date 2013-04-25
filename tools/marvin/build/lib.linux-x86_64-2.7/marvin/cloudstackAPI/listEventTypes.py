
"""List Event Types"""
from baseCmd import *
from baseResponse import *
class listEventTypesCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class listEventTypesResponse (baseResponse):
    def __init__(self):
        """Event Type"""
        self.name = None

