
"""Deletes a LB stickiness policy."""
from baseCmd import *
from baseResponse import *
class deleteLBStickinessPolicyCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """the ID of the LB stickiness policy"""
        """Required"""
        self.id = None
        self.required = ["id",]

class deleteLBStickinessPolicyResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

