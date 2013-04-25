
"""Creates resource tag(s)"""
from baseCmd import *
from baseResponse import *
class createTagsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "true"
        """list of resources to create the tags for"""
        """Required"""
        self.resourceids = []
        """type of the resource"""
        """Required"""
        self.resourcetype = None
        """Map of tags (key/value pairs)"""
        """Required"""
        self.tags = []
        """identifies client specific tag. When the value is not null, the tag can't be used by cloudStack code internally"""
        self.customer = None
        self.required = ["resourceids","resourcetype","tags",]

class createTagsResponse (baseResponse):
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        """true if operation is executed successfully"""
        self.success = None

