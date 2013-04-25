
"""Deleting resource tag(s)"""
from baseCmd import *
from baseResponse import *
class deleteTagsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """Delete tags for resource id(s)"""
        """Required"""
        self.resourceids = []
        """Delete tag by resource type"""
        """Required"""
        self.resourcetype = None
        """Delete tags matching key/value pairs"""
        self.tags = []
        self.required = ["resourceids","resourcetype",]

class deleteTagsResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

