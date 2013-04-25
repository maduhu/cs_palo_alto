
"""Deletes a static route"""
from baseCmd import *
from baseResponse import *
class deleteStaticRouteCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the static route"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteStaticRouteResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

