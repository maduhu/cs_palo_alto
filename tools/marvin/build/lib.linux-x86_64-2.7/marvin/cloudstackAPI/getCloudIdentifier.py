
"""Retrieves a cloud identifier."""
from baseCmd import *
from baseResponse import *
class getCloudIdentifierCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """the user ID for the cloud identifier"""
        """Required"""
        self.userid = None
        self.required = ["userid",]

class getCloudIdentifierResponse (baseResponse):
    def __init__(self):
        """the cloud identifier"""
        self.cloudidentifier = None
        """the signed response for the cloud identifier"""
        self.signature = None
        """the user ID for the cloud identifier"""
        self.userid = None

