
"""Lists implementors of implementor of a network traffic type or implementors of all network traffic types"""
from baseCmd import *
from baseResponse import *
class listTrafficTypeImplementorsCmd (baseCmd):
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        """"""
        self.page = None
        """"""
        self.pagesize = None
        """Optional. The network traffic type, if specified, return its implementor. Otherwise, return all traffic types with their implementor"""
        self.traffictype = None
        self.required = []

class listTrafficTypeImplementorsResponse (baseResponse):
    def __init__(self):
        """network traffic type"""
        self.traffictype = None
        """implementor of network traffic type"""
        self.traffictypeimplementor = None

